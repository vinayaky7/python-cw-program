def parse_to_float(s):
    try:
        return float(s)
    except ValueError as e:
        print(f"Error parsing '{s}' to float: {e}")
        return None

def parse_to_int(s):
    try:
        return int(s)
    except ValueError as e:
        print(f"Error parsing '{s}' to int: {e}")
        return None

def main():
    try:
        # Parsing to float examples
        s_float = "3.14"
        float_value = parse_to_float(s_float)
        if float_value is not None:
            print(f"Parsed '{s_float}' to float:", float_value)

        s_float_error = "abc"
        float_value_error = parse_to_float(s_float_error)
        if float_value_error is not None:
            print(f"Parsed '{s_float_error}' to float:", float_value_error)

        # Parsing to int examples
        s_int = "42"
        int_value = parse_to_int(s_int)
        if int_value is not None:
            print(f"Parsed '{s_int}' to int:", int_value)

        s_int_error = "123abc"
        int_value_error = parse_to_int(s_int_error)
        if int_value_error is not None:
            print(f"Parsed '{s_int_error}' to int:", int_value_error)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
