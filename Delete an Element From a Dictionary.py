#####Using del Keyword:
def delete_from_dict(d, key):
    try:
        del d[key]
        print(f"Deleted key '{key}' from the dictionary.")
    except KeyError:
        print(f"Key '{key}' not found in the dictionary.")
    except Exception as e:
        print(f"Error deleting key '{key}' from the dictionary: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        my_dict = {'a': 1, 'b': 2, 'c': 3}

        # Delete key 'b' from the dictionary
        delete_from_dict(my_dict, 'b')

        # Try to delete a non-existent key
        delete_from_dict(my_dict, 'x')

        # Print the updated dictionary
        print("Updated dictionary:", my_dict)

    except Exception as e:
        print(f"Error: {e}")







# ##################Using dict.pop() Method:
# def delete_from_dict_pop(d, key):
#     try:
#         value = d.pop(key)
#         print(f"Deleted key '{key}' with value '{value}' from the dictionary.")
#     except KeyError:
#         print(f"Key '{key}' not found in the dictionary.")
#     except Exception as e:
#         print(f"Error deleting key '{key}' from the dictionary using pop: {e}")
#
# # Example usage:
# if __name__ == "__main__":
#     try:
#         my_dict = {'a': 1, 'b': 2, 'c': 3}
#
#         # Delete key 'b' using pop method
#         delete_from_dict_pop(my_dict, 'b')
#
#         # Try to delete a non-existent key
#         delete_from_dict_pop(my_dict, 'x')
#
#         # Print the updated dictionary
#         print("Updated dictionary:", my_dict)
#
#     except Exception as e:
#         print(f"Error: {e}")
