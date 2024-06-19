import os

def create_nested_directory(directory_path):
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Successfully created the directory: {directory_path}")
    except OSError as e:
        print(f"Error: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        directory_path = input("Enter the full path for the nested directory: ")
        create_nested_directory(directory_path)
    except Exception as e:
        print(f"Error: {e}")
