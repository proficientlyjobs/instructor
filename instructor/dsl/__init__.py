from .iterable import IterableModel
from .maybe import Maybe
from .partial import Partial
from .citation import CitationMixin
from .simple_type import is_simple_type, ModelAdapter

__all__ = [  # noqa: F405
    "CitationMixin",
    "IterableModel",
    "Maybe",
    "Partial",
    "is_simple_type",
    "ModelAdapter",
    "validators",
    "function_calls",
    "validators_module",
]


def __getattr__(name: str):
    """Lazy import for backwards compatibility."""
    if name == "validators":
        from ..processing import validators

        return validators
    elif name == "function_calls":
        from ..processing import function_calls

        return function_calls
    elif name == "validators_module":
        from .. import validation as validators_module

        return validators_module
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
