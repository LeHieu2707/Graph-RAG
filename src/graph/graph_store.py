class GraphStore:

    def __init__(self):
        self.graph = {}

    def add_edge(self, entity1, relation, entity2):

        if entity1 not in self.graph:
            self.graph[entity1] = []

        self.graph[entity1].append((relation, entity2))

    def get_neighbors(self, entity):

        return self.graph.get(entity, [])