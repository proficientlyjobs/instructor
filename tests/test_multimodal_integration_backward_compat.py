"""
Integration tests for multimodal backward compatibility.

These tests verify that actual multimodal functionality works correctly
when using the deprecated import paths.
"""

import pytest
import warnings
from pathlib import Path
from unittest.mock import patch, MagicMock


class TestMultimodalIntegrationBackwardCompat:
    """Integration tests for multimodal backward compatibility."""

    def test_image_creation_with_old_imports(self):
        """Test that Image class from old import path works for creating instances."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # Focus on functionality, not warnings
            
            from instructor.multimodal import Image
            
            # Test URL creation
            url = "https://example.com/image.jpg"
            image = Image.from_url(url)
            assert image.source == url
            assert image.media_type == "image/jpeg"
            assert image.data is None

    def test_audio_creation_with_old_imports(self):
        """Test that Audio class from old import path works for creating instances."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            
            from instructor.multimodal import Audio
            
            # Test URL creation
            url = "https://example.com/audio.wav"
            audio = Audio.from_url(url)
            assert audio.source == url
            assert audio.media_type == "audio/wav"
            assert audio.data is None

    def test_pdf_creation_with_old_imports(self):
        """Test that PDF class from old import path works for creating instances."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            
            from instructor.multimodal import PDF
            
            # Test URL creation
            url = "https://example.com/document.pdf"
            pdf = PDF.from_url(url)
            assert pdf.source == url
            assert pdf.media_type == "application/pdf"
            assert pdf.data is None

    def test_base64_image_with_old_imports(self):
        """Test base64 image creation through old import path."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            
            from instructor.multimodal import Image
            
            # Test base64 creation
            base64_data = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/wAALCAABAAEBAREA/8QAFAABAAAAAAAAAAAAAAAAAAAACf/EABQQAQAAAAAAAAAAAAAAAAAAAAD/2gAIAQEAAD8AKp//2Q=="
            image = Image.from_base64(base64_data)
            assert image.media_type == "image/jpeg"
            assert image.data is not None

    def test_autodetect_functionality_with_old_imports(self):
        """Test that autodetect functions work through old import path."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            
            from instructor.multimodal import autodetect_media
            
            # Test with a URL that should be detected as an image
            url = "https://example.com/image.jpg"
            result = autodetect_media(url)
            
            # Should return the same URL since it's just a string
            assert result == url

    def test_path_based_creation_with_old_imports(self, tmp_path: Path):
        """Test file path based creation through old import path."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            
            from instructor.multimodal import Image
            
            # Create a fake image file
            image_path = tmp_path / "test_image.jpg"
            image_path.write_bytes(b"fake image data")
            
            image = Image.from_path(image_path)
            assert image.source == image_path
            assert image.media_type == "image/jpeg"
            assert image.data is not None

    def test_mime_type_constants_with_old_imports(self):
        """Test that MIME type constants work through old import path."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            
            from instructor.multimodal import VALID_MIME_TYPES, VALID_AUDIO_MIME_TYPES, VALID_PDF_MIME_TYPES
            
            # Test that constants contain expected values
            assert "image/jpeg" in VALID_MIME_TYPES
            assert "image/png" in VALID_MIME_TYPES
            assert "audio/wav" in VALID_AUDIO_MIME_TYPES
            assert "audio/mp3" in VALID_AUDIO_MIME_TYPES
            assert "application/pdf" in VALID_PDF_MIME_TYPES

    @patch('instructor.processing.multimodal.requests.get')
    def test_url_image_with_old_imports(self, mock_get):
        """Test URL-based image creation with old imports (mocked)."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            
            from instructor.multimodal import Image
            
            # Mock the response
            mock_response = MagicMock()
            mock_response.content = b"fake image data"
            mock_response.headers = {"Content-Type": "image/jpeg"}
            mock_response.raise_for_status.return_value = None
            mock_get.return_value = mock_response
            
            # This should work with the old import
            image = Image.from_url("https://example.com/image.jpg")
            assert image.source == "https://example.com/image.jpg"
            assert image.media_type == "image/jpeg"

    def test_mixed_import_styles_work_together(self):
        """Test that mixing old and new import styles works correctly."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            
            # Import some from old path
            from instructor.multimodal import PDF, Image
            
            # Import some from new path
            from instructor.processing.multimodal import Audio
            
            # All should be available and functional
            assert PDF is not None
            assert Image is not None
            assert Audio is not None
            
            # Should be able to create instances
            pdf = PDF.from_url("https://example.com/doc.pdf")
            image = Image.from_url("https://example.com/image.jpg")
            audio = Audio.from_url("https://example.com/audio.wav")
            
            assert pdf.source == "https://example.com/doc.pdf"
            assert image.source == "https://example.com/image.jpg"
            assert audio.source == "https://example.com/audio.wav"

    def test_lazy_import_only_warns_on_access(self):
        """Test that warnings are only issued when attributes are actually accessed."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            
            # Just importing the module shouldn't generate warnings
            import instructor.multimodal  # noqa: F401
            initial_warning_count = len(w)
            
            # Accessing an attribute should generate a warning
            from instructor.multimodal import PDF  # noqa: F401
            after_access_count = len(w)
            
            # Should have more warnings after accessing the attribute
            assert after_access_count > initial_warning_count

    def test_all_expected_exports_available(self):
        """Test that all expected exports are available through the old import path."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            
            expected_exports = [
                "PDF", "Image", "Audio",
                "ImageParamsBase", "ImageParams", 
                "CacheControlType", "OptionalCacheControlType",
                "VALID_MIME_TYPES", "VALID_AUDIO_MIME_TYPES", "VALID_PDF_MIME_TYPES",
                "autodetect_media", "convert_contents", "convert_messages",
                "extract_genai_multimodal_content"
            ]
            
            for export_name in expected_exports:
                try:
                    module = __import__("instructor.multimodal", fromlist=[export_name])
                    attr = getattr(module, export_name)
                    assert attr is not None, f"{export_name} should be available"
                except AttributeError:
                    pytest.fail(f"Expected export '{export_name}' not available through backward compatibility shim")

    def test_warning_issued_per_attribute_access(self):
        """Test that deprecation warnings are issued for each unique attribute access."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            
            # Access different attributes
            from instructor.multimodal import PDF  # noqa: F401
            from instructor.multimodal import Image  # noqa: F401
            from instructor.multimodal import Audio  # noqa: F401
            
            # Should have multiple deprecation warnings
            deprecation_warnings = [warning for warning in w if issubclass(warning.category, DeprecationWarning)]
            assert len(deprecation_warnings) >= 3  # At least one per class accessed