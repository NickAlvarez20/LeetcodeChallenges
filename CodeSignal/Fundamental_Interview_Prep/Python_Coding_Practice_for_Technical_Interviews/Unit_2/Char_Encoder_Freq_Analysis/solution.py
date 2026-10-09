from collections import Counter

def solution(sentence):
    result = []
    final_result = []

    for i in range(len(sentence)):
        # lowercase
        if sentence[i].isalnum() and sentence[i].islower():
            new_char = ((ord(sentence[i])-ord('a') - 1) % 26) + ord('a')
            result.append(chr(new_char))
        # uppercase
        elif sentence[i].isalnum() and sentence[i].isupper():
            new_char = ((ord(sentence[i])-ord('A') - 1) % 26) + ord('A')
            result.append(chr(new_char))
        # digits
        elif sentence[i].isalnum() and sentence[i].isdigit():
            new_char = ((ord(sentence[i])-ord('0') - 1) % 10) + ord('0')
            result.append(chr(new_char))

    # now create a counter, convert key to ascii value, subtract the frequency, and return abs calculation
    freq_chars = Counter(result)
    for key, val in freq_chars.items():
        ascii_val = ord(key)
        final_result.append(abs(ascii_val-val))

    return sorted(final_result)



    

print(solution("Hello, 123!"))
