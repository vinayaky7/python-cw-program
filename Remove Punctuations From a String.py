def remove_punctuations(input_string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punctuations = ""
    for char in input_string:
        if char not in punctuations:
            no_punctuations += char
    return no_punctuations

# Example usage:
try:
    input_string = input("Enter a string: ")
    result_string = remove_punctuations(input_string)
    print(f"String without punctuations: {result_string}")
except Exception as e:
    print(f"Error: {e}")
