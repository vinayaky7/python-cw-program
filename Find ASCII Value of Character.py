try:
    # Input a character from the user
    char = input("Enter a character: ")

    # Using ord() to find ASCII value
    ascii_value = ord(char)

    # Print the ASCII value
    print(f"The ASCII value of '{char}' is: {ascii_value}")
except TypeError:
    print("Please enter a single character.")
