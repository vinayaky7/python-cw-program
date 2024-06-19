def read_file_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()  # Read all lines into a list
            return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


# Example usage:
if __name__ == "__main__":
    try:
        filename = "example.txt"
        lines = read_file_lines(filename)

        if lines:
            print(f"Contents of file '{filename}':")
            for line in lines:
                print(line.strip())  # Strip newline character for cleaner output
        else:
            print(f"No content read from file '{filename}'.")

    except Exception as e:
        print(f"Error: {e}")
