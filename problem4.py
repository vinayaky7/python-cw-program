#print content of directory using os module
import os

def print_directory_contents(path):
    try:
        # List all the files and directories in the specified path
        directory_contents = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in directory_contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"The path '{path}' is not a directory.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")

# Example usage
path_to_directory = '/'  # Change this to the desired directory path
print_directory_contents(path_to_directory)
