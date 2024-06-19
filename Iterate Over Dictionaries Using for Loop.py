def main():
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # Iterating over keys
    print("Iterating over keys:")
    for key in my_dict:
        print(key)

    # Iterating over values
    print("\nIterating over values:")
    for value in my_dict.values():
        print(value)

    # Iterating over both keys and values
    print("\nIterating over both keys and values:")
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")

if __name__ == "__main__":
    main()
