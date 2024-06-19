def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage:
if __name__ == "__main__":
    input_list = [1, 3, 2, 1, 5, 2, 7, 8, 3]
    unique_list = remove_duplicates(input_list)
    print(f"Original list: {input_list}")
    print(f"List with duplicates removed: {unique_list}")
