def concatenate_lists_operator(list1, list2):
    return list1 + list2

def concatenate_lists_extend(list1, list2):
    list1.extend(list2)
    return list1

def main():
    try:
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]

        # Concatenate using + operator
        concatenated_list_operator = concatenate_lists_operator(list1, list2)
        print("Concatenated List using + operator:", concatenated_list_operator)

        # Concatenate using extend method
        list1 = [1, 2, 3]  # Reset list1 for extend method usage
        concatenated_list_extend = concatenate_lists_extend(list1, list2)
        print("Concatenated List using extend method:", concatenated_list_extend)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
