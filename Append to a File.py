def append_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content + "\n")  # Append content to the file with a newline
        print(f"Appended '{content}' to {filename}")
    except Exception as e:
        print(f"Error appending to {filename}: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        filename = "example.txt"
        content_to_append = "This is new content."

        append_to_file(filename, content_to_append)

        # Verify the content has been appended by reading the file
        with open(filename, 'r') as file:
            print(f"Current content of {filename}:")
            for line in file:
                print(line.strip())

    except Exception as e:
        print(f"Error: {e}")

