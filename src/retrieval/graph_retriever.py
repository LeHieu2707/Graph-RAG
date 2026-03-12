class GraphRetriever:

    def __init__(self, graph_store):
        self.graph_store = graph_store

    def expand_entities(self, entities):

        expanded = []

        for e in entities:
            neighbors = self.graph_store.get_neighbors(e)
            expanded.extend(neighbors)

        return expanded