def count_vowels(input_string):
    # Initialize counters for each vowel
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0

    # Convert input string to lowercase to handle both uppercase and lowercase vowels
    input_string = input_string.lower()

    # Iterate through each character in the string
    for char in input_string:
        if char == 'a':
            count_a += 1
        elif char == 'e':
            count_e += 1
        elif char == 'i':
            count_i += 1
        elif char == 'o':
            count_o += 1
        elif char == 'u':
            count_u += 1

    # Display the counts of each vowel
    print(f"Count of 'a': {count_a}")
    print(f"Count of 'e': {count_e}")
    print(f"Count of 'i': {count_i}")
    print(f"Count of 'o': {count_o}")
    print(f"Count of 'u': {count_u}")


# Example usage:
if __name__ == "__main__":
    try:
        input_string = input("Enter a string: ")
        count_vowels(input_string)
    except Exception as e:
        print(f"Error: {e}")
