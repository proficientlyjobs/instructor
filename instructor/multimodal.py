"""
Backward compatibility shim for instructor.multimodal imports.

This module provides backward compatibility for the old import path:
    from instructor.multimodal import PDF, Image, Audio

The new import path is:
    from instructor.processing.multimodal import PDF, Image, Audio

This shim will be removed in a future major version (v2.0.0).
"""

import warnings

# Import all multimodal classes from the new location
from instructor.processing.multimodal import (
    PDF,
    Image,
    Audio,
    ImageParamsBase,
    ImageParams,
    CacheControlType,
    OptionalCacheControlType,
    VALID_MIME_TYPES,
    VALID_AUDIO_MIME_TYPES,
    VALID_PDF_MIME_TYPES,
    autodetect_media,
    convert_contents,
    convert_messages,
    extract_genai_multimodal_content,
)

# Issue deprecation warning when this module is imported
warnings.warn(
    "Importing from 'instructor.multimodal' is deprecated and will be removed in v2.0.0. "
    "Please update your imports to use 'instructor.processing.multimodal' instead:\n"
    "  from instructor.processing.multimodal import PDF, Image, Audio",
    DeprecationWarning,
    stacklevel=2
)

# Make all imports available at module level for backward compatibility
__all__ = [
    "PDF",
    "Image", 
    "Audio",
    "ImageParamsBase",
    "ImageParams",
    "CacheControlType",
    "OptionalCacheControlType",
    "VALID_MIME_TYPES",
    "VALID_AUDIO_MIME_TYPES",
    "VALID_PDF_MIME_TYPES",
    "autodetect_media",
    "convert_contents",
    "convert_messages",
    "extract_genai_multimodal_content",
]