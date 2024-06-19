def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    # Check if lengths are different
    if len(str1) != len(str2):
        return False

    # Count frequency of each character
    frequency = {}
    for char in str1:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Compare with second string
    for char in str2:
        if char in frequency:
            frequency[char] -= 1
        else:
            return False

    # Check if all counts are zero
    for count in frequency.values():
        if count != 0:
            return False

    return True


# Example usage:
if __name__ == "__main__":
    s1 = "Listen"
    s2 = "Silent"

    if are_anagrams(s1, s2):
        print(f"{s1} and {s2} are anagrams.")
    else:
        print(f"{s1} and {s2} are not anagrams.")
