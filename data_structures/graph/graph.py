class Graph:

    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self._adjacency_list[value] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight = 0):
        
        if start_vertex not in self._adjacency_list: 
            raise KeyError('No start vertex')
        
        if end_vertex not in self._adjacency_list:
            raise KeyError('No end vertex')

        adjancies = self._adjacency_list[start_vertex]
        adjancies.append((end_vertex, weight))

    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def length(self):
        return len(self._adjacency_list)


class Vertex:

    def __init__(self, value):
        self.value = value

if __name__ == "__main__":
    g = Graph()
    g.add_node('rice')
    g.add_node('spam')
    g.add_edge('spam', 'rice', 2)
    print(g.length())
    print(g.get_nodes())
    print(g._adjacency_list)





