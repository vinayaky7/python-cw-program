########################Method 1: Using string slicing and upper()##############################
def capitalize_first_char(s):
    return s[0].upper() + s[1:] if s else ''

# Example usage:
if __name__ == "__main__":
    string = "hello, world!"
    capitalized_string = capitalize_first_char(string)
    print(f"Original string: {string}")
    print(f"Capitalized string: {capitalized_string}")


# ##############################Method 2: Using capitalize() method##############################
# def capitalize_first_char(s):
#     return s.capitalize()
#
# # Example usage:
# if __name__ == "__main__":
#     string = "hello, world!"
#     capitalized_string = capitalize_first_char(string)
#     print(f"Original string: {string}")
#     print(f"Capitalized string: {capitalized_string}")
