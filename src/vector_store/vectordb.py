import numpy as np

class VectorDB:

    def __init__(self):
        self.vectors = []
        self.texts = []

    def add(self, embeddings, texts):
        self.vectors.extend(embeddings)
        self.texts.extend(texts)

    def search(self, query_vector, top_k=5):
        scores = []

        for i, vec in enumerate(self.vectors):
            score = np.dot(query_vector, vec)
            scores.append((score, self.texts[i]))

        scores.sort(reverse=True)
        return scores[:top_k]