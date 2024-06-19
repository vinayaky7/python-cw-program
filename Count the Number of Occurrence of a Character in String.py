def count_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

# Example usage:
if __name__ == "__main__":
    input_string = "hello, world!"
    character_to_count = 'o'
    occurrences = count_occurrences(input_string, character_to_count)
    print(f"Number of occurrences of '{character_to_count}' in '{input_string}': {occurrences}")
