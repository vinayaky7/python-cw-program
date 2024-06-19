def count_occurrences(lst, item):
    try:
        return lst.count(item)
    except Exception as e:
        print(f"Error: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    try:
        my_list = [1, 2, 3, 4, 2, 2, 3, 1, 5]
        item_to_count = 2

        count = count_occurrences(my_list, item_to_count)
        print(
            f"Number of occurrences of {item_to_count} in the list: {count}")  # Output: Number of occurrences of 2 in the list: 3

        # Testing with a string list
        str_list = ["apple", "banana", "apple", "cherry", "banana", "date", "apple"]
        str_to_count = "apple"

        count_str = count_occurrences(str_list, str_to_count)
        print(
            f"Number of occurrences of '{str_to_count}' in the list: {count_str}")  # Output: Number of occurrences of 'apple' in the list: 3

    except Exception as e:
        print(f"Error: {e}")
