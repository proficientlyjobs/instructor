"""
Example demonstrating per-call hooks in Instructor.

This example shows how to use hooks at the individual call level,
combining them with client-level hooks for flexible event handling.
"""

import instructor
import openai
import pydantic
from instructor.core.hooks import Hooks


class User(pydantic.BaseModel):
    """A simple user model."""

    name: str
    age: int


def create_client_hooks() -> Hooks:
    """Create hooks that will be attached to the client."""
    hooks = Hooks()

    def log_all_requests(*_args, **kwargs):
        print(
            f"🌐 [CLIENT] All requests go through here: model={kwargs.get('model', 'unknown')}"
        )

    def log_all_responses(response):
        print(f"🌐 [CLIENT] All responses logged here")
        _ = response  # Acknowledge we received the response

    def log_all_errors(error):
        print(f"🌐 [CLIENT] All errors logged: {type(error).__name__}")

    hooks.on("completion:kwargs", log_all_requests)
    hooks.on("completion:response", log_all_responses)
    hooks.on("completion:error", log_all_errors)
    hooks.on("parse:error", log_all_errors)

    return hooks


def create_debug_hooks() -> Hooks:
    """Create hooks for debugging specific calls."""
    hooks = Hooks()

    def debug_request(*_args, **kwargs):
        messages = kwargs.get("messages", [])
        print(f"🐛 [DEBUG] Debugging this specific call:")
        print(f"🐛 [DEBUG] - Message count: {len(messages)}")
        print(f"🐛 [DEBUG] - Temperature: {kwargs.get('temperature', 'default')}")

    def debug_response(response):
        print(f"🐛 [DEBUG] Response details:")
        print(f"🐛 [DEBUG] - Model used: {getattr(response, 'model', 'unknown')}")
        if hasattr(response, "usage") and response.usage:
            print(f"🐛 [DEBUG] - Tokens: {response.usage.total_tokens}")
        _ = response  # Acknowledge we received the response

    hooks.on("completion:kwargs", debug_request)
    hooks.on("completion:response", debug_response)

    return hooks


def create_performance_hooks() -> Hooks:
    """Create hooks for performance monitoring specific calls."""
    hooks = Hooks()

    import time

    start_time = None

    def perf_start(**_kwargs):
        nonlocal start_time
        start_time = time.time()
        print(f"⏱️  [PERF] Starting performance measurement")

    def perf_end(_response):
        nonlocal start_time
        if start_time:
            duration = time.time() - start_time
            print(f"⏱️  [PERF] Call completed in {duration:.2f}s")

    hooks.on("completion:kwargs", perf_start)
    hooks.on("completion:response", perf_end)

    return hooks


def main():
    """Demonstrate per-call hooks combined with client hooks."""

    # Create client with global hooks
    client_hooks = create_client_hooks()
    client = instructor.from_openai(openai.OpenAI(), hooks=client_hooks)

    print("=== Example 1: Regular call (only client hooks) ===")
    try:
        user = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Extract: Alice is 25 years old"}],
            response_model=User,
        )
        print(f"Result: {user}\n")
    except Exception as e:
        print(f"Exception: {e}\n")

    print("=== Example 2: Call with debug hooks ===")
    debug_hooks = create_debug_hooks()
    try:
        user = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Extract: Bob is 30 years old"}],
            response_model=User,
            temperature=0.7,
            hooks=debug_hooks,  # Add debug hooks for this specific call
        )
        print(f"Result: {user}\n")
    except Exception as e:
        print(f"Exception: {e}\n")

    print("=== Example 3: Call with performance monitoring ===")
    perf_hooks = create_performance_hooks()
    try:
        user = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Extract: Charlie is 35 years old"}],
            response_model=User,
            hooks=perf_hooks,  # Add performance hooks for this specific call
        )
        print(f"Result: {user}\n")
    except Exception as e:
        print(f"Exception: {e}\n")

    print("=== Example 4: Call with combined debug + performance hooks ===")
    # Combine multiple per-call hooks
    combined_hooks = debug_hooks + perf_hooks
    try:
        user = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Extract: Diana is 28 years old"}],
            response_model=User,
            temperature=0.3,
            hooks=combined_hooks,  # Multiple per-call hooks combined
        )
        print(f"Result: {user}\n")
    except Exception as e:
        print(f"Exception: {e}\n")

    print("=== Example 5: Another regular call (client hooks still work) ===")
    try:
        user = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Extract: Eve is 22 years old"}],
            response_model=User,
        )
        print(f"Result: {user}\n")
    except Exception as e:
        print(f"Exception: {e}\n")

    print("=== Example 6: Per-call hooks with create_partial ===")
    try:
        print("Using create_partial with debug hooks:")
        for partial_user in client.chat.completions.create_partial(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Extract: Frank is 40 years old"}],
            response_model=User,
            hooks=debug_hooks,  # Per-call hooks work with create_partial too
        ):
            print(f"Partial result: {partial_user}")
        print()
    except Exception as e:
        print(f"Exception: {e}\n")


if __name__ == "__main__":
    main()
