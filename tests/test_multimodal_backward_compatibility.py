"""
Tests for backward compatibility of instructor.multimodal imports.

This test module verifies that the old import path continues to work
with proper deprecation warnings while maintaining identical functionality.
"""

import pytest
import warnings
from unittest.mock import patch


class TestMultimodalBackwardCompatibility:
    """Test backward compatibility for multimodal imports."""

    def test_old_import_path_works(self):
        """Test that the old import path still works."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            
            # This should work without raising ImportError
            from instructor.multimodal import PDF, Image, Audio
            
            # Verify classes are available
            assert PDF is not None
            assert Image is not None
            assert Audio is not None
            
            # Should have issued deprecation warning
            assert len(w) > 0
            assert any(issubclass(warning.category, DeprecationWarning) for warning in w)

    def test_new_import_path_still_works(self):
        """Test that the new import path continues to work."""
        # This should work without any warnings or errors
        from instructor.processing.multimodal import PDF, Image, Audio
        
        assert PDF is not None
        assert Image is not None
        assert Audio is not None

    def test_classes_are_identical(self):
        """Test that old and new import paths provide identical classes."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # Suppress deprecation warnings for this test
            
            from instructor.multimodal import PDF as OldPDF, Image as OldImage, Audio as OldAudio
            from instructor.processing.multimodal import PDF as NewPDF, Image as NewImage, Audio as NewAudio
            
            # Classes should be exactly the same object
            assert OldPDF is NewPDF
            assert OldImage is NewImage  
            assert OldAudio is NewAudio

    def test_deprecation_warning_content(self):
        """Test that the deprecation warning contains helpful content."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            
            from instructor.multimodal import PDF
            
            # Should have at least one warning
            assert len(w) > 0
            
            # Find the deprecation warning
            deprecation_warnings = [warning for warning in w if issubclass(warning.category, DeprecationWarning)]
            assert len(deprecation_warnings) > 0
            
            warning_msg = str(deprecation_warnings[0].message)
            
            # Should mention the deprecated path
            assert "instructor.multimodal" in warning_msg
            # Should mention the new path
            assert "instructor.processing.multimodal" in warning_msg
            # Should mention version removal
            assert "v2.0.0" in warning_msg

    def test_multiple_imports_from_old_path(self):
        """Test importing multiple classes from the old path."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            
            from instructor.multimodal import PDF, Image, Audio
            
            # All classes should be available
            assert PDF is not None
            assert Image is not None
            assert Audio is not None
            
            # Should have deprecation warnings for each access
            assert len(w) > 0

    def test_constants_available_through_shim(self):
        """Test that constants are available through the backward compatibility shim."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # Suppress warnings for this test
            
            from instructor.multimodal import VALID_MIME_TYPES, VALID_AUDIO_MIME_TYPES, VALID_PDF_MIME_TYPES
            
            # Should be available and non-empty
            assert VALID_MIME_TYPES
            assert VALID_AUDIO_MIME_TYPES
            assert VALID_PDF_MIME_TYPES
            
            # Should contain expected values
            assert "image/jpeg" in VALID_MIME_TYPES
            assert "audio/wav" in VALID_AUDIO_MIME_TYPES
            assert "application/pdf" in VALID_PDF_MIME_TYPES

    def test_utility_functions_available_through_shim(self):
        """Test that utility functions are available through the backward compatibility shim."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # Suppress warnings for this test
            
            from instructor.multimodal import autodetect_media, convert_contents
            
            # Functions should be available
            assert callable(autodetect_media)
            assert callable(convert_contents)

    def test_nonexistent_attribute_raises_error(self):
        """Test that accessing non-existent attributes raises AttributeError."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # Suppress warnings for this test
            
            with pytest.raises(AttributeError, match="module 'instructor.multimodal' has no attribute 'NonExistentClass'"):
                from instructor.multimodal import NonExistentClass  # noqa: F401

    def test_lazy_import_behavior(self):
        """Test that imports are lazy and only happen when accessed."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            
            # Just importing the module shouldn't trigger warnings yet
            import instructor.multimodal  # noqa: F401
            
            # No warnings should be issued until we access an attribute
            pre_access_warnings = len(w)
            
            # Now access an attribute - this should trigger the warning
            from instructor.multimodal import PDF  # noqa: F401
            
            # Should have more warnings now
            post_access_warnings = len(w)
            assert post_access_warnings > pre_access_warnings

    def test_warning_stack_level(self):
        """Test that warnings point to the user's code, not internal implementation."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            
            from instructor.multimodal import Image  # noqa: F401
            
            # Should have warning
            assert len(w) > 0
            deprecation_warning = next(warning for warning in w if issubclass(warning.category, DeprecationWarning))
            
            # Warning should point to this test file, not the shim implementation
            assert "test_multimodal_backward_compatibility.py" in deprecation_warning.filename

    @pytest.mark.parametrize("class_name", ["PDF", "Image", "Audio"])
    def test_individual_class_imports(self, class_name):
        """Test that each multimodal class can be imported individually."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # Suppress warnings for this test
            
            # Dynamic import to test each class
            module = __import__("instructor.multimodal", fromlist=[class_name])
            cls = getattr(module, class_name)
            
            assert cls is not None
            assert hasattr(cls, "__name__")
            assert cls.__name__ == class_name