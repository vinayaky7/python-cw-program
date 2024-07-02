def sort_dict_by_value(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    return sorted_dict

# Example usage:
if __name__ == "__main__":
    try:
        my_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1}
        sorted_dict = sort_dict_by_value(my_dict)
        print("Sorted Dictionary by Value (Ascending):", sorted_dict)
    except Exception as e:
        print(f"Error: {e}")
