import re


def is_float_try_except(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_float_regex(s):
    return bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', s))


def main():
    try:
        test_strings = ["3.14", "123", "abc", "-0.5", "+42.0", ".25", "-.75", "1.0e3", "-2.5e-2"]

        print("Checking float numbers using try-except approach:")
        for s in test_strings:
            print(f"{s}: {is_float_try_except(s)}")

        print("\nChecking float numbers using regex:")
        for s in test_strings:
            print(f"{s}: {is_float_regex(s)}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
