def main():
    my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    # Example 1: Basic Slicing
    slice1 = my_list[2:5]
    slice2 = my_list[:4]
    slice3 = my_list[6:]

    print("Example 1: Basic Slicing")
    print("Slice 1:", slice1)  # Output: ['c', 'd', 'e']
    print("Slice 2:", slice2)  # Output: ['a', 'b', 'c', 'd']
    print("Slice 3:", slice3)  # Output: ['g', 'h', 'i']
    print()

    # Example 2: Negative Indices and Step
    slice4 = my_list[2:7:2]
    slice5 = my_list[-1:2:-1]
    slice6 = my_list[::-1]

    print("Example 2: Negative Indices and Step")
    print("Slice 4:", slice4)  # Output: ['c', 'e', 'g']
    print("Slice 5:", slice5)  # Output: ['i', 'h', 'g']
    print("Slice 6 (Reverse List):", slice6)  # Output: ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    print()

if __name__ == "__main__":
    main()

