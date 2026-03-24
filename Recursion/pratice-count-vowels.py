def count_vowels(s: str) -> int:
    if not s:
        return 0
    
    # Look at very first char
    
    if s[0].lower in "aeiou":
        current_vowel_count += 1
    else:
        current_vowel_count = 0

    # 2. Get the answer for the rest of the string
    result_of_the_rest = count_vowels(s[1:])

    # 3. Combine them
    return current_vowel_count + result_of_the_rest
