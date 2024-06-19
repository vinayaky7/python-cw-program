def get_substring(s, start, end):
    try:
        return s[start:end]
    except IndexError:
        print("Error: Index out of range")
        return None


# Example usage:
if __name__ == "__main__":
    try:
        original_string = "Hello, World!"

        # Get substring from index 1 to 5 (exclusive)
        substring1 = get_substring(original_string, 1, 5)
        print("Substring 1:", substring1)  # Output: Substring 1: ello

        # Get substring from index 7 to end
        substring2 = get_substring(original_string, 7, len(original_string))
        print("Substring 2:", substring2)  # Output: Substring 2: World!

        # Get substring from index 7 to 12 (end index exceeds string length)
        substring3 = get_substring(original_string, 7, 12)
        print("Substring 3:", substring3)  # Output: Substring 3: World

        # Handling invalid indices
        substring4 = get_substring(original_string, 15, 20)
        print("Substring 4:", substring4)  # Output: Error: Index out of range, Substring 4: None

    except Exception as e:
        print(f"Error: {e}")
