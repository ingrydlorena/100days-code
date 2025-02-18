'''
Day 51: Graphs
Implement a graph data structure.
'''

class Graph:
    def __init__(self, directed = False):
        #Initialize an empty dictionary to store the graph
        self.graph = {}
        #Boolean to determine if the graph is directed pr undirected
        self.directed = directed

    def add_node(self,node):
        #Adds a node to the graph
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self, node1, node2):
        
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)

        #Adds an edge from node1 to node2
        self.graph[node1].append(node2)

        if not self.directed:
            self.graph[node2].append(node1)
    
    def display(self):
        # Display the entire graph
        for node, neighbors in self.graph.items():
            print(f"{node}:{','.join(neighbors)}")

#example
if __name__ == "__main__":
    #Create an undirected graph
    g = Graph(directed=False)

    #Add nodes and edges
    g.add_node('A')
    g.add_node('B')
    g.add_node('W')
    g.add_edge('B', 'C')
    g.add_edge('F', 'G')
    g.add_edge('Z', 'W')

    print('Graph:')
    g.display()

    print("\n Directed Graph:")
    g2 = Graph(directed=True)
    g2.add_edge('B', 'E')
    g2.add_edge("B", 'D')
    g2.add_edge('Z', 'H')
    g2.display()

        
