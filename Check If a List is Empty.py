def is_list_empty_method1(my_list):
    return not my_list

def is_list_empty_method2(my_list):
    return len(my_list) == 0

def main():
    try:
        # Test cases
        empty_list = []
        non_empty_list = [1, 2, 3]

        # Using Method 1: if not my_list
        print("Using Method 1 (if not my_list):")
        print("Is empty_list empty?", is_list_empty_method1(empty_list))  # Output: True
        print("Is non_empty_list empty?", is_list_empty_method1(non_empty_list))  # Output: False
        print()

        # Using Method 2: len(my_list) == 0
        print("Using Method 2 (len(my_list) == 0):")
        print("Is empty_list empty?", is_list_empty_method2(empty_list))  # Output: True
        print("Is non_empty_list empty?", is_list_empty_method2(non_empty_list))  # Output: False
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
