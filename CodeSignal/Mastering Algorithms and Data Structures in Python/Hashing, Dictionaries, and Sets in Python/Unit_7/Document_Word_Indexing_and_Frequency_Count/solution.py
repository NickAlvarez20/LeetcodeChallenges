def keyword_index(docs):
    count_dict = {}

    for doc_idx, doc in enumerate(docs):
        for word in doc.split():
            if word in count_dict:
                if doc_idx in count_dict[word]:
                    count_dict[word][doc_idx] += 1
                else:
                    count_dict[word][doc_idx] = 1
            else:
                count_dict[word] = {doc_idx: 1}

    return count_dict


docs = ["Hello world", "world of python", "python is a snake"]
print(
    keyword_index(docs)
)  # Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}
