def sort_words_alphabetically(input_string):
    # Split the string into words
    words = input_string.split()

    # Sort the words alphabetically
    words_sorted = sorted(words)

    # Join the sorted words back into a string
    sorted_string = ' '.join(words_sorted)

    return sorted_string

# Example usage:
try:
    input_string = input("Enter a string: ")
    sorted_string = sort_words_alphabetically(input_string)
    print(f"Sorted words in alphabetical order: {sorted_string}")
except Exception as e:
    print(f"Error: {e}")
