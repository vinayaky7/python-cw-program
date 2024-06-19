def lists_to_dict(keys, values):
    try:
        # Using zip() function to pair elements from keys and values lists
        dictionary = {keys[i]: values[i] for i in range(min(len(keys), len(values)))}
        return dictionary
    except Exception as e:
        print(f"Error converting lists to dictionary: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    try:
        keys = ['a', 'b', 'c']
        values = [1, 2, 3]

        result_dict = lists_to_dict(keys, values)
        print("Resulting dictionary:", result_dict)

        # Adding more keys than values
        keys_extra = ['x', 'y', 'z', 'w']
        values_extra = [10, 20]
        result_dict_extra = lists_to_dict(keys_extra, values_extra)
        print("Resulting dictionary with extra keys:", result_dict_extra)

        # Adding more values than keys
        keys_few = ['p', 'q']
        values_few = [100, 200, 300]
        result_dict_few = lists_to_dict(keys_few, values_few)
        print("Resulting dictionary with few values:", result_dict_few)

    except Exception as e:
        print(f"Error: {e}")
