import os
import shutil

def move_file(source_path, destination_path):
    """
    Move a file from source path to destination path.
    
    Args:
        source_path (str): Relative path to the source file
        destination_path (str): Relative path to the destination directory
    
    Raises:
        FileNotFoundError: If the source file does not exist
        IsADirectoryError: If the source path is a directory
        PermissionError: If there are insufficient permissions to move the file
    """
    # Normalize paths to handle potential cross-platform issues
    source_path = os.path.normpath(source_path)
    destination_path = os.path.normpath(destination_path)
    
    # Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file {source_path} does not exist")
    
    # Check if source is a file, not a directory
    if not os.path.isfile(source_path):
        raise IsADirectoryError(f"Source path {source_path} is not a file")
    
    # Ensure destination directory exists, create if not
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    # Move the file
    try:
        shutil.move(source_path, destination_path)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot move {source_path} to {destination_path}")
    
    return True