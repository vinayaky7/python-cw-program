def check_key_in_dict(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

# Example usage:
if __name__ == "__main__":
    try:
        my_dict = {'a': 1, 'b': 2, 'c': 3}

        # Check if 'b' is present in my_dict
        key_to_check = 'b'
        if check_key_in_dict(my_dict, key_to_check):
            print(f"Key '{key_to_check}' is present in the dictionary.")
        else:
            print(f"Key '{key_to_check}' is not present in the dictionary.")

        # Check if 'd' is present in my_dict
        key_to_check = 'd'
        if check_key_in_dict(my_dict, key_to_check):
            print(f"Key '{key_to_check}' is present in the dictionary.")
        else:
            print(f"Key '{key_to_check}' is not present in the dictionary.")

    except Exception as e:
        print(f"Error: {e}")
