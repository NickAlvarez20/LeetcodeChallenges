import numpy as np

# 1. The "Internet" Dataset (More patterns to learn)
data = """
ai is cool ai is fast ai is smart
coding is fun coding is power coding is logic
flowers are red flowers are blue flowers are pretty
ai is the future coding is the way
"""
words = data.lower().split()

# 2. Build a Vocabulary (The unique words the model knows)
vocab = sorted(list(set(words)))
word_to_int = {w: i for i, w in enumerate(vocab)}
int_to_word = {i: w for i, w in enumerate(vocab)}
v_size = len(vocab)

# 3. Training: Building the Probability Matrix
# Rows = Current Word, Columns = Possible Next Words
matrix = np.zeros((v_size, v_size))

# 4. Training (The .fit phase)
# We slide through the text and count how often words follow each other
for i in range(len(words) - 1):
    current_word_idx = word_to_int[words[i]]
    next_word_idx = word_to_int[words[i + 1]]
    matrix[current_word_idx, next_word_idx] += 1

# Normalize rows so they sum to 1.0 (probabilities)
# We add a tiny value (1e-9) to avoid dividing by zero
probs = matrix / (matrix.sum(axis=1, keepdims=True) + 1e-9)

print(f"LLM Trained! Vocabulary size: {v_size} words.\n")


# 6. Predict! (The .predict phase)
def test_llm(input_word):
    input_word = input_word.lower()
    # Change word_to_idx -> word_to_int
    if input_word not in word_to_int:
        return f"'{input_word}' is not in my vocabulary!"

    # Change word_to_idx -> word_to_int
    row_idx = word_to_int[input_word]
    row_probs = probs[row_idx]

    # Find the most likely next word
    best_guess_idx = np.argmax(row_probs)
    # Change idx_to_word -> int_to_word
    best_word = int_to_word[best_guess_idx]
    confidence = row_probs[best_guess_idx] * 100

    return f"Input: '{input_word}' -> Next Word: '{best_word}' ({confidence:.1f}% confidence)"


# --- DYNAMIC TESTS ---
print(test_llm("ai"))  # Should predict 'is'
print(test_llm("coding"))  # Should predict 'is'
print(test_llm("flowers"))  # Should predict 'are'
print(test_llm("is"))
