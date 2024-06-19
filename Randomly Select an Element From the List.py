import random


def random_element_from_list(input_list):
    try:
        if input_list:
            return random.choice(input_list)
        else:
            return None  # Return None if the list is empty
    except Exception as e:
        print(f"Error: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    try:
        my_list = ["apple", "banana", "cherry", "date", "elderberry"]

        # Randomly select an element from the list
        random_element = random_element_from_list(my_list)

        if random_element:
            print("Randomly selected element:", random_element)
        else:
            print("The list is empty.")

    except Exception as e:
        print(f"Error: {e}")
