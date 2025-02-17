import os
import pytest
import shutil
from src.file_mover import move_file

@pytest.fixture
def setup_test_files(tmp_path):
    # Create a source directory with a test file
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    test_file = source_dir / "test_file.txt"
    test_file.write_text("Test content")
    
    # Create a destination directory
    dest_dir = tmp_path / "destination"
    dest_dir.mkdir()
    
    return {
        "source_dir": str(source_dir),
        "dest_dir": str(dest_dir),
        "source_file": str(test_file),
        "dest_file": str(dest_dir / "test_file.txt")
    }

def test_move_file_success(setup_test_files):
    """Test successful file move"""
    result = move_file(
        setup_test_files["source_file"], 
        setup_test_files["dest_file"]
    )
    assert result is True
    assert os.path.exists(setup_test_files["dest_file"])
    assert not os.path.exists(setup_test_files["source_file"])

def test_move_file_nonexistent_source(tmp_path):
    """Test moving a non-existent file"""
    with pytest.raises(FileNotFoundError):
        move_file(
            str(tmp_path / "nonexistent.txt"), 
            str(tmp_path / "destination" / "file.txt")
        )

def test_move_file_source_is_directory(tmp_path):
    """Test attempting to move a directory"""
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    
    with pytest.raises(IsADirectoryError):
        move_file(
            str(test_dir), 
            str(tmp_path / "destination" / "dir")
        )

def test_move_file_automatically_creates_destination_dir(setup_test_files):
    """Test that destination directory is created if it doesn't exist"""
    new_dest = os.path.join(setup_test_files["dest_dir"], "new_subdir", "moved_file.txt")
    result = move_file(
        setup_test_files["source_file"], 
        new_dest
    )
    assert result is True
    assert os.path.exists(new_dest)
    assert not os.path.exists(setup_test_files["source_file"])