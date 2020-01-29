# Graph
Implementation

## Challenge
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

* add_node()
    * Adds a new node to the graph
    * Takes in the value of that node
    * Returns the added node
* add_edge()
    * Adds a new edge between two nodes in the graph
    * Include the ability to have a “weight”
    * Takes in the two nodes to be connected by the edge
    * Both nodes should already be in the Graph
* get_nodes()
    * Returns all of the nodes in the graph as a collection (set, list, or similar)
* get_neigbors()
    * Returns a collection of nodes connected to the given node
    * Takes in a given node
    * Include the weight of the connection in the returned collection
* size()
    * Returns the total number of nodes in the graph

## Approach & Efficiency
* `class Graph`
    * `add_node(value)`: O(1)
    * `add_edge(start, end, weight)`: O(1)
    * `get_nodes()`: O(1)
    * `get_neigbors(node)`: O(1)
    * `size(key)`: O(1)