#!/usr/bin/env python3

"""
Example demonstrating comprehensive retry tracking in Instructor.

This example shows how to access detailed information about all failed attempts
when retries are exhausted, including:
- All exceptions that occurred during retries
- The completion responses for each failed attempt
- Attempt numbers for debugging

Run with: python example.py
"""

import instructor
from openai import OpenAI
from pydantic import BaseModel, Field
from instructor.core.exceptions import InstructorRetryException
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax


class UserInfo(BaseModel):
    """User information with strict validation that will likely fail."""

    name: str = Field(..., description="Full name of the user")
    age: int = Field(..., ge=0, le=150, description="Age must be between 0 and 150")
    email: str = Field(
        ..., pattern=r"^[^@]+@[^@]+\.[^@]+$", description="Valid email address"
    )
    phone: str = Field(
        ...,
        pattern=r"^\+?1?-?\d{3}-?\d{3}-?\d{4}$",
        description="Valid US phone number",
    )


def main():
    console = Console()

    # Initialize the client with a high retry count to see multiple failures
    client = instructor.from_openai(OpenAI())

    # This prompt is intentionally vague to cause validation failures
    messages = [
        {
            "role": "user",
            "content": "Extract user info from this text: 'John is 25 years old and can be reached at john@email and phone 555-1234'",
        }
    ]

    console.print(
        Panel.fit(
            "Starting extraction with intentionally problematic data...",
            style="bold blue",
        )
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            response_model=UserInfo,
            messages=messages,
            max_retries=3,  # Allow multiple retries to demonstrate tracking
            temperature=0.7,  # Add some randomness to get different failures
        )

        console.print(
            Panel.fit(
                "✅ Success! This shouldn't happen with our test data.",
                style="bold green",
            )
        )
        console.print(response)

    except InstructorRetryException as e:
        console.print(
            Panel.fit(
                "❌ All retries exhausted! Let's examine the failures:",
                style="bold red",
            )
        )

        # Display basic retry information
        console.print(f"\n📊 [bold]Retry Summary:[/bold]")
        console.print(f"   • Total attempts: {e.n_attempts}")
        console.print(f"   • Final exception: {type(e.args[0]).__name__}")
        console.print(f"   • Total usage: {e.total_usage}")

        # Display detailed information about each failed attempt
        console.print(f"\n🔍 [bold]Detailed Failure Analysis:[/bold]")

        for _i, failed_attempt in enumerate(e.failed_attempts, 1):
            console.print(
                f"\n[bold yellow]Attempt {failed_attempt.attempt_number}:[/bold yellow]"
            )

            # Show the exception details
            console.print(f"   Exception: {type(failed_attempt.exception).__name__}")
            console.print(f"   Message: {str(failed_attempt.exception)}")

            # Show completion details if available
            if failed_attempt.completion and hasattr(
                failed_attempt.completion, "choices"
            ):
                try:
                    content = failed_attempt.completion.choices[0].message.content
                    if content:
                        # Pretty print the raw response
                        console.print("   Raw Response:")
                        syntax = Syntax(
                            content, "json", theme="monokai", line_numbers=True
                        )
                        console.print(syntax)
                except Exception as parse_error:
                    console.print(f"   Raw Response: [Could not parse: {parse_error}]")

            # For validation errors, show specific field issues
            if hasattr(failed_attempt.exception, "errors"):
                console.print("   Validation Errors:")
                for error in failed_attempt.exception.errors():
                    console.print(
                        f"      • {error.get('loc', 'unknown')}: {error.get('msg', 'unknown error')}"
                    )

        # Show how this can be used programmatically
        console.print(f"\n🔧 [bold]Programmatic Access:[/bold]")
        console.print("You can now access all this data programmatically:")

        code_example = """
# Access all failed attempts
for attempt in exception.failed_attempts:
    print(f"Attempt {attempt.attempt_number}: {attempt.exception}")
    if attempt.completion:
        # Process the raw completion response
        analyze_completion(attempt.completion)

# Count specific error types
validation_errors = [
    a for a in exception.failed_attempts 
    if 'ValidationError' in str(type(a.exception))
]
print(f"Validation errors: {len(validation_errors)}")
        """

        syntax = Syntax(code_example.strip(), "python", theme="monokai")
        console.print(syntax)


if __name__ == "__main__":
    main()
