def bytes_to_string(bytes_data, encoding='utf-8'):
    try:
        decoded_string = bytes_data.decode(encoding)
        return decoded_string
    except UnicodeDecodeError:
        print(f"Error decoding bytes with {encoding} encoding")
        return None

# Example usage:
if __name__ == "__main__":
    bytes_data = b'Hello, world!'
    string_data = bytes_to_string(bytes_data)
    print(f"Original bytes: {bytes_data}")
    print(f"Decoded string: {string_data}")
