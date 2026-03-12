class VectorRetriever:

    def __init__(self, vectordb, embedder):
        self.vectordb = vectordb
        self.embedder = embedder

    def retrieve(self, query):

        query_vec = self.embedder.embed([query])[0]

        results = self.vectordb.search(query_vec)

        return [r[1] for r in results]