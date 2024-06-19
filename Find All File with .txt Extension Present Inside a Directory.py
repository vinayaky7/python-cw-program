import os

def find_txt_files(directory):
    txt_files = []
    # Iterate through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(os.path.join(root, file))
    return txt_files


# Example usage:
if __name__ == "__main__":
    directory = "/path/to/your/directory"  # Replace with your directory path
    txt_files = find_txt_files(directory)

    if txt_files:
        print(f"Text files found in '{directory}':")
        for txt_file in txt_files:
            print(txt_file)
    else:
        print(f"No text files found in '{directory}'")
