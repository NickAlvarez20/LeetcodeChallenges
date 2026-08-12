def find_anagram_words(list_1, list_2):
    # edge case - convert to lowercase, use list comprehension
    lowercase_list_1 = [word.lower() for word in list_1]
    lowercase_list_2 = [word.lower() for word in list_2]

    # convert every word from both lists to a sorted tuple of its characters using list comprehension
    sorted_tuples_1 = set(tuple(sorted(word)) for word in lowercase_list_1)
    sorted_tuples_2 = set(tuple(sorted(word)) for word in lowercase_list_2)
    print(sorted_tuples_1, sorted_tuples_2)

    # use intersection operator to find common elements
    common_tuples = sorted_tuples_1 & sorted_tuples_2

    # iterate over words in the original lists, for each word, if sorted tuple is present in common_tuples set, add it to respective output list
    list_1_output = [
        word for word in lowercase_list_1 if tuple(sorted(word)) in common_tuples
    ]  # shuffles each word and matches against the common tuples list
    list_2_output = [
        word for word in lowercase_list_2 if tuple(sorted(word)) in common_tuples
    ]

    # finally, return a list of tuples where each tuple is an anagram pair from list1 and list 2
    output = set()

    for word1 in list_1_output:
        for word2 in list_2_output:
            # traversing every pair of words in filtered lists
            if tuple(sorted(word1)) == tuple(sorted(word2)):
                output.add(word1)
    return list(output)


print(
    find_anagram_words(["cinema", "iceman"], ["iceman", "cinema"])
)  # should return ['cinema', 'iceman']
print(find_anagram_words(["test", "stet"], ["tent", "nett"]))  # should return []
print(find_anagram_words(["hello", "world"], ["dolly", "sir"]))  # should return []
