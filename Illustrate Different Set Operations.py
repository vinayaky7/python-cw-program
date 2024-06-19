def set_operations(set1, set2):
    # Union
    union_set = set1 | set2
    print(f"Union of set1 and set2: {union_set}")

    # Intersection
    intersection_set = set1 & set2
    print(f"Intersection of set1 and set2: {intersection_set}")

    # Difference (set1 - set2)
    difference_set1 = set1 - set2
    print(f"Difference (set1 - set2): {difference_set1}")

    # Difference (set2 - set1)
    difference_set2 = set2 - set1
    print(f"Difference (set2 - set1): {difference_set2}")

    # Symmetric Difference
    symmetric_difference_set = set1 ^ set2
    print(f"Symmetric Difference of set1 and set2: {symmetric_difference_set}")

    # Subset check
    subset_check = set1 <= set2
    print(f"Is set1 a subset of set2?: {subset_check}")

    # Superset check
    superset_check = set1 >= set2
    print(f"Is set1 a superset of set2?: {superset_check}")

    # Disjoint check
    disjoint_check = set1.isdisjoint(set2)
    print(f"Are set1 and set2 disjoint?: {disjoint_check}")


# Example usage:
if __name__ == "__main__":
    try:
        # Input sets
        set1 = {1, 2, 3, 4, 5}
        set2 = {3, 4, 5, 6, 7}

        # Display initial sets
        print(f"Set 1: {set1}")
        print(f"Set 2: {set2}")

        # Perform set operations
        set_operations(set1, set2)

    except Exception as e:
        print(f"Error: {e}")
