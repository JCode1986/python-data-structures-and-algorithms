from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def empty(self):
        return len(self.dq) == 0

class Graph:

    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """
        Graph method that takes in a value as a parameter, and adds that value to the graph as the key, and an empty list as the value
            Args: (1) value
            In: value
            Out: {value, empty list}
        """

        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight = 0):
        """
        Graph method that takes 2 vertex's, one for the start and other for the end. Also takes in weight.
            Args: (3) - vertex, vertex, weight        
            In: instance, instance, integer
            Out: tuple with end vertex as key, and weight as value added graph if both vertex's are present
        """
        if start_vertex not in self._adjacency_list.keys(): 
            raise KeyError('Start Vertex not in Graph')
        
        if end_vertex not in self._adjacency_list.keys():
            raise KeyError('End Vertex not in Graph')

        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append((end_vertex, weight))

    def get_nodes(self):
        """
        Graph method that returns all of the nodes in the graph as a collection
            Args: None
            In: None
            Out: dictionary with key value pair
        """

        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        """
        Graph method that returns a collection of nodes connected to the given node
            Args: (1) vertex
            In: instance
            Out: tuple with key value pair inside a list 
        """

        return self._adjacency_list[vertex]

    def size(self):
        """
        Graph method that returns the total number of nodes in the graph
            Args: None
            In: None
            Out: integer 
        """        
        return len(self._adjacency_list)


    def breadth_first(self, vertex):
        """
        Graph method that traverses the graph and returns vertices in level order
            Args: 1
            In: vertex
            Out: list 
        """
        nodes = []
        queue = Queue()

        if vertex not in self._adjacency_list:
            raise ValueError

        queue.enqueue(vertex)

        while not queue.empty():
            front = queue.dequeue()
            nodes.append(front)

            for child, _ in self.get_neighbors(front):
                if child not in nodes:
                    child.visited = True
                    queue.enqueue(child)

        for node in self._adjacency_list:
            node.visited = False

        return nodes

    def depth_first(self, vertex):
        """
        Graph method that traverses the graph and returns vertices in depth order
            Args: 1
            In: vertex
            Out: list 
        """
        nodes = []
        stack = []

        if vertex not in self._adjacency_list:
            raise ValueError

        stack.append(vertex)

        while stack:
            top = stack.pop()
            nodes.append(top)

            for child, _ in self.get_neighbors(top):
                if child not in nodes:
                    child.visited = True
                    stack.append(child)

        for node in self._adjacency_list:
            node.visited = False

        return nodes

    def get_edges(self, v_lst):

        def contains_vertex(value, lst):
            for vertex in lst:
                if isinstance(vertex, tuple):
                    if vertex[0].value == value:
                        return vertex
                    continue
                if vertex.value == value:
                    return vertex
            return False, 0

        current = contains_vertex(v_lst[0], self._adjacency_list.keys())
        if isinstance(current, Vertex):
            edge_weight = 0
            for index in range(1, len(v_lst)):
                current, cost = contains_vertex(v_lst[index], self.get_neighbors(current))
                edge_weight += cost
                if not current:
                    return (False, '$0')
            return (True, f'${edge_weight}')
        return (False, '$0')



class Vertex:

    def __init__(self, value):
        self.value = value
        self.visited = False
        self.next = None

    def __repr__(self):
        return self.value


if __name__ == "__main__":
    g = Graph()
    rice = g.add_node('rice')
    spam = g.add_node('spam')
    end = g.add_node('end')
    start = g.add_node('start')
    veggies = g.add_node('veggies')
    print(g._adjacency_list)
    print(g.get_nodes())
    g.add_edge(start, end, '$2')
    g.add_edge(start, rice, '$23')
    g.add_edge(spam, rice, '$420')
    g.add_edge(end, veggies, '$1986')
    g.add_edge(veggies, spam, '$1986')
    print(g.size())
    print(g.get_nodes())
    print(g._adjacency_list)
    print(g.get_neighbors(start))
    print(g.breadth_first(start))
    print(g.depth_first(start))
    # print(g.get_edges(g._adjacency_list))
