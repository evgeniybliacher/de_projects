
from pathlib import Path


def is_valid_string(value: str) -> bool:
    """
    Validate that the provided value is a non-empty string.

    Args:
        value (str): The string to validate.

    Returns:
        bool: True if the string is non-empty, False otherwise.
    """
    return isinstance(value, str) and bool(value.strip())

def is_valid_url(url: str) -> bool:
    """
    Validate that the provided value is a valid URL.

    Args:
        url (str): The URL to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    return is_valid_string(url) and (url.startswith("http://") or url.startswith("https://"))

def is_valid_file_path(path: str) -> bool:
    """
    Validate that the provided value is a valid file path.

    Args:
        path (str): The file path to validate.  
    Returns:
        bool: True if the file path is valid, False otherwise.
    """
    return is_valid_string(path) and Path(path).exists()

def is_folder_empty(folder_path: str) -> bool:
    """
    Check if the specified folder is empty.

    Args:
        folder_path (str): The path to the folder.

    Returns:
        bool: True if the folder is empty, False otherwise.
    """
    import os
    return os.path.isdir(folder_path) and not os.listdir(folder_path)

def is_file_exists(file_path: str) -> bool:
    """
    Check if the specified file exists.

    Args:
        file_path (str): The path to the file.
    Returns:
        bool: True if the file exists, False otherwise.
    """
    import os
    return os.path.isfile(file_path)
    