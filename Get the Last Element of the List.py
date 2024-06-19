def get_last_element(lst):
    if lst:
        return lst[-1]  # Returns the last element of the list
    else:
        return None  # Handle empty list scenario

def get_last_element_with_pop(lst):
    try:
        return lst.pop()  # Removes and returns the last element of the list
    except IndexError:
        return None  # Handle empty list scenario

def main():
    try:
        # Using indexing method
        my_list = [1, 2, 3, 4, 5]
        last_element = get_last_element(my_list)
        print("Using indexing - Last element of the list:", last_element)  # Output: Last element of the list: 5

        # Using pop method
        my_list = [1, 2, 3, 4, 5]
        last_element_pop = get_last_element_with_pop(my_list)
        print("Using pop() - Last element of the list:", last_element_pop)  # Output: Last element of the list: 5
        print("Modified list:", my_list)  # Output: Modified list: [1, 2, 3, 4]

        # Handling empty list
        empty_list = []
        last_element_empty = get_last_element(empty_list)
        print("Using indexing - Last element of the empty list:", last_element_empty)  # Output: Last element of the empty list: None

        empty_list = []
        last_element_empty_pop = get_last_element_with_pop(empty_list)
        print("Using pop() - Last element of the empty list:", last_element_empty_pop)  # Output: Last element of the empty list: None

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
