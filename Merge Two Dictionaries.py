###Using update() Method:
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Make a copy of dict1 to preserve original
    merged_dict.update(dict2)  # Update with contents of dict2
    return merged_dict


# Example usage:
if __name__ == "__main__":
    try:
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}

        merged_dict = merge_dicts(dict1, dict2)
        print("Merged dictionary:", merged_dict)
    except Exception as e:
        print(f"Error: {e}")



#####Using Dictionary Unpacking (**):
# def merge_dicts(dict1, dict2):
#     merged_dict = {**dict1, **dict2}
#     return merged_dict


# Example usage:
# if __name__ == "__main__":
#     try:
#         dict1 = {'a': 1, 'b': 2}
#         dict2 = {'c': 3, 'd': 4}
#
#         merged_dict = merge_dicts(dict1, dict2)
#         print("Merged dictionary:", merged_dict)
#     except Exception as e:
#         print(f"Error: {e}")
