import numpy as np

# 1. Our "Internet" (The Training Data)
text = "ai is cool ai is fast ai is smart"
words = text.split()

# 2. Build a Vocabulary (The unique words the model knows)
vocab = sorted(list(set(words)))
word_to_int = {w: i for i, w in enumerate(vocab)}
int_to_word = {i: w for i, w in enumerate(vocab)}

# 3. Create the "Brain" (A Matrix of zeros)
# Rows = Current Word (X), Columns = Next Word (Y)
brain = np.zeros((len(vocab), len(vocab)))

# 4. Training (The .fit phase)
# We slide through the text and count how often words follow each other
for i in range(len(words) - 1):
    current_word_idx = word_to_int[words[i]]
    next_word_idx = word_to_int[words[i + 1]]
    brain[current_word_idx, next_word_idx] += 1

# 5. Convert counts to Probabilities (Confidence)
# This makes each row add up to 1.0 (100%)
brain_norm = brain / brain.sum(axis=1, keepdims=True)


# 6. Predict! (The .predict phase)
def generate_next_word(current_word):
    idx = word_to_int[current_word]
    probabilities = brain_norm[idx]

    # Pick the word with the highest probability (Confidence)
    next_idx = np.argmax(probabilities)
    return int_to_word[next_idx], probabilities[next_idx]


# Test it out
word = "ai"
prediction, confidence = generate_next_word(word)

print(f"Current Word (X): {word}")
print(f"Predicted Next Word (Y): {prediction}")
print(f"Confidence: {confidence*100:.1f}%")
