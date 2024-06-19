import os

def get_file_extension(filename):
    try:
        _, extension = os.path.splitext(filename)
        return extension.lower()  # Convert to lowercase if needed
    except Exception as e:
        print(f"Error extracting extension from {filename}: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    try:
        filename1 = "example.txt"
        filename2 = "image.png"
        filename3 = "script.py"

        extension1 = get_file_extension(filename1)
        extension2 = get_file_extension(filename2)
        extension3 = get_file_extension(filename3)

        print(f"Extension of {filename1}: {extension1}")  # Output: Extension of example.txt: .txt
        print(f"Extension of {filename2}: {extension2}")  # Output: Extension of image.png: .png
        print(f"Extension of {filename3}: {extension3}")  # Output: Extension of script.py: .py

    except Exception as e:
        print(f"Error: {e}")
