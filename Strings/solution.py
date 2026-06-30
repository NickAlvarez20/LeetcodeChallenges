def solution(sentences, words):
    result_arr = []

    # 1. use zip for pairing up the lists with perfect index access for each loop
    for sentence, word in zip(sentences, words):
        sentence_lower = sentence.lower()
        word_lower = word.lower()
        start_pos = sentence_lower.find(word_lower)
        curr_index = 0
        result_pieces = []

        while start_pos != -1:
            result_pieces.append(sentence[curr_index:start_pos])

            # Grab the original word slice exactly as it is cased
            original_word_slice = sentence[start_pos:start_pos + len(word)]
            flipped = original_word_slice[::-1]

            # Check if the original word started with a capital

            if original_word_slice[0].isupper():
                flipped = flipped.capitalize()

            result_pieces.append(flipped)

            curr_index = start_pos + len(word)
            start_pos = sentence_lower.find(word_lower, curr_index)

        result_pieces.append(sentence[curr_index:])
        result_arr.append("".join(result_pieces))

    return result_arr


print(
    solution(
        [
            "this is a simple example.",
            "the name is bond. james bond.",
            "remove every single e",
        ],
        ["simple", "bond", "e"],
    ),
    [
        "this is a elpmis example.",
        "the name is dnob. james dnob.",
        "remove every single e",
    ],
)
