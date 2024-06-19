import os


def get_file_size(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # Get the file size in bytes
        file_size = os.path.getsize(file_path)
        return file_size
    else:
        return None  # File does not exist


# Example usage:
if __name__ == "__main__":
    file_path = 'example.txt'  # Replace with your file path
    size_in_bytes = get_file_size(file_path)

    if size_in_bytes is not None:
        print(f"File size of '{file_path}': {size_in_bytes} bytes")
    else:
        print(f"File '{file_path}' not found")
