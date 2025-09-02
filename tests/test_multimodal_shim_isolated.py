"""
Isolated tests for multimodal backward compatibility shim.

These tests validate the shim structure and lazy import pattern
without requiring external dependencies.
"""

import ast
import warnings
from pathlib import Path


def test_shim_file_structure():
    """Test that the shim file has the correct structure."""
    shim_path = Path(__file__).parent.parent / "instructor" / "multimodal.py"
    
    with open(shim_path, 'r') as f:
        source = f.read()
    
    # Verify syntax
    tree = ast.parse(source)
    
    # Check for required components
    assert '__getattr__' in source, "Should have __getattr__ function for lazy imports"
    assert 'warnings.warn' in source, "Should have warnings.warn call"
    assert 'DeprecationWarning' in source, "Should use DeprecationWarning"
    assert 'stacklevel=2' in source, "Should use proper stack level"
    assert 'instructor.processing.multimodal' in source, "Should reference new import location"
    
    # Verify function structure
    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    assert '__getattr__' in functions, "Should have __getattr__ function"


def test_shim_docstring():
    """Test that the shim has proper documentation."""
    shim_path = Path(__file__).parent.parent / "instructor" / "multimodal.py"
    
    with open(shim_path, 'r') as f:
        source = f.read()
    
    tree = ast.parse(source)
    docstring = ast.get_docstring(tree)
    
    assert docstring is not None, "Should have module docstring"
    assert 'backward' in docstring.lower() or 'compatibility' in docstring.lower(), "Should mention compatibility"


def test_warning_message_format():
    """Test that the warning message has the expected format."""
    shim_path = Path(__file__).parent.parent / "instructor" / "multimodal.py"
    
    with open(shim_path, 'r') as f:
        source = f.read()
    
    # The warning should contain helpful migration information
    assert "instructor.multimodal" in source, "Should mention deprecated path"
    assert "instructor.processing.multimodal" in source, "Should mention new path"
    assert "v2.0.0" in source, "Should mention removal version"
    assert "from instructor.processing.multimodal import" in source, "Should show exact import syntax"


if __name__ == "__main__":
    test_shim_file_structure()
    print("✅ Shim structure test passed")
    
    test_shim_docstring()
    print("✅ Shim docstring test passed")
    
    test_warning_message_format()
    print("✅ Warning format test passed")
    
    print("\n🎉 All isolated shim tests passed!")