def first_non_repeating_char(s: str) -> str:
    # 1. Build a frequency map (count occurrences of each char)
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # 2. Iterate through the string again to find the first char with count 1
    for char in s:
        if char_count[char] == 1:
            return char

    return "No non-repeating character found"


# Test Cases
print(f"swiss -> {first_non_repeating_char('swiss')}")  # Output: w
print(f"aabbcccd -> {first_non_repeating_char('aabbcccd')}")  # Output: d