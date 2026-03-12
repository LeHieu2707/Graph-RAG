class Reranker:

    def rerank(self, query, documents):

        scored = []

        for doc in documents:
            score = doc.count(query)

            scored.append((score, doc))

        scored.sort(reverse=True)

        return [d[1] for d in scored]