##########Using strip()
def trim_whitespace(s):
    return s.strip()

# Example usage:
if __name__ == "__main__":
    s = "  Hello, World!  "
    trimmed_string = trim_whitespace(s)
    print(f"Original string: '{s}'")
    print(f"Trimmed string: '{trimmed_string}'")

# ############Using rstrip() and lstrip()############################################
# def trim_whitespace_custom(s):
#     return s.rstrip().lstrip()
#
# # Example usage:
# if __name__ == "__main__":
#     s = "  Hello, World!  "
#     trimmed_string = trim_whitespace_custom(s)
#     print(f"Original string: '{s}'")
#     print(f"Trimmed string (custom): '{trimmed_string}'")
#
#
# #########Using Regular Expressions (re module)#########################################
# import re
#
# def trim_whitespace_regex(s):
#     return re.sub(r'^\s+|\s+$', '', s)
#
# # Example usage:
# if __name__ == "__main__":
#     s = "  Hello, World!  "
#     trimmed_string = trim_whitespace_regex(s)
#     print(f"Original string: '{s}'")
#     print(f"Trimmed string (regex): '{trimmed_string}'")

