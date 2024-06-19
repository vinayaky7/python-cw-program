import shutil

def copy_file(source_file, destination_file):
    try:
        shutil.copy(source_file, destination_file)
        print(f"File copied successfully from '{source_file}' to '{destination_file}'.")
    except IOError as e:
        print(f"Unable to copy file. Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        source_file = 'D:\source.txt'  # Replace with your source file path
        destination_file = 'destination.txt'  # Replace with your destination file path

        copy_file(source_file, destination_file)
    except Exception as e:
        print(f"Error: {e}")
