"""
Example demonstrating how to combine hooks in Instructor.

This example shows three different ways to combine hooks:
1. Using the + operator to create a new combined hooks instance
2. Using the += operator to add hooks to an existing instance
3. Using the Hooks.combine() class method to combine multiple instances
"""

import instructor
import openai
import pydantic
from instructor.core.hooks import Hooks


class User(pydantic.BaseModel):
    """A simple user model."""

    name: str
    age: int


def create_logging_hooks() -> Hooks:
    """Create a hooks instance focused on logging."""
    hooks = Hooks()

    def log_request(**kwargs):
        print(f"🔍 [LOGGING] Request: model={kwargs.get('model', 'unknown')}")

    def log_response(response):
        print(f"✅ [LOGGING] Response received successfully")
        _ = response  # Acknowledge we received the response

    def log_error(error):
        print(f"❌ [LOGGING] Error: {type(error).__name__}: {str(error)}")

    hooks.on("completion:kwargs", log_request)
    hooks.on("completion:response", log_response)
    hooks.on("completion:error", log_error)
    hooks.on("parse:error", log_error)

    return hooks


def create_metrics_hooks() -> Hooks:
    """Create a hooks instance focused on metrics collection."""
    hooks = Hooks()

    # Simple metrics collector
    metrics = {"requests": 0, "responses": 0, "errors": 0, "tokens": 0}

    def count_request(*_args, **_kwargs):
        metrics["requests"] += 1
        print(f"📊 [METRICS] Total requests: {metrics['requests']}")

    def count_response(response):
        metrics["responses"] += 1
        if hasattr(response, "usage") and response.usage:
            tokens = response.usage.total_tokens
            metrics["tokens"] += tokens
            print(f"📊 [METRICS] Tokens used: {tokens}, Total: {metrics['tokens']}")
        print(f"📊 [METRICS] Total responses: {metrics['responses']}")

    def count_error(_error):
        metrics["errors"] += 1
        print(f"📊 [METRICS] Total errors: {metrics['errors']}")

    hooks.on("completion:kwargs", count_request)
    hooks.on("completion:response", count_response)
    hooks.on("completion:error", count_error)
    hooks.on("parse:error", count_error)

    return hooks


def create_debug_hooks() -> Hooks:
    """Create a hooks instance focused on debugging."""
    hooks = Hooks()

    def debug_request(*_args, **kwargs):
        print(f"🐛 [DEBUG] Messages: {len(kwargs.get('messages', []))} messages")

    def debug_response(response):
        print(f"🐛 [DEBUG] Response ID: {getattr(response, 'id', 'unknown')}")

    def debug_error(error):
        print(f"🐛 [DEBUG] Error details: {error}")

    hooks.on("completion:kwargs", debug_request)
    hooks.on("completion:response", debug_response)
    hooks.on("completion:error", debug_error)
    hooks.on("parse:error", debug_error)

    return hooks


def main():
    """Demonstrate different ways to combine hooks."""

    # Create individual hook instances
    logging_hooks = create_logging_hooks()
    metrics_hooks = create_metrics_hooks()
    debug_hooks = create_debug_hooks()

    print("=== Example 1: Using + operator ===")

    # Combine using + operator (creates new instance)
    combined_hooks = logging_hooks + metrics_hooks

    client = instructor.from_openai(openai.OpenAI(), hooks=combined_hooks)

    try:
        user = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Extract: Alice is 25 years old"}],
            response_model=User,
        )
        print(f"Result: {user}\n")
    except Exception as e:
        print(f"Exception: {e}\n")

    print("=== Example 2: Using += operator ===")

    # Start with logging hooks and add metrics hooks
    combined_hooks_2 = create_logging_hooks()
    combined_hooks_2 += metrics_hooks

    client2 = instructor.from_openai(openai.OpenAI(), hooks=combined_hooks_2)

    try:
        user = client2.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Extract: Bob is 30 years old"}],
            response_model=User,
        )
        print(f"Result: {user}\n")
    except Exception as e:
        print(f"Exception: {e}\n")

    print("=== Example 3: Using Hooks.combine() class method ===")

    # Combine all three using class method
    all_combined = Hooks.combine(logging_hooks, metrics_hooks, debug_hooks)

    client3 = instructor.from_openai(openai.OpenAI(), hooks=all_combined)

    try:
        user = client3.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Extract: Charlie is 35 years old"}],
            response_model=User,
        )
        print(f"Result: {user}\n")
    except Exception as e:
        print(f"Exception: {e}\n")

    print("=== Example 4: Creating a copy and modifying ===")

    # Create a copy and add additional hooks
    copied_hooks = logging_hooks.copy()
    copied_hooks.on(
        "completion:kwargs",
        lambda *_args, **_kwargs: print("🔄 [COPY] Additional hook"),
    )

    client4 = instructor.from_openai(openai.OpenAI(), hooks=copied_hooks)

    try:
        user = client4.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Extract: Diana is 28 years old"}],
            response_model=User,
        )
        print(f"Result: {user}")
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
