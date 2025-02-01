'''
Day 58: Depth-first search (DFS) algorithm
Implement a depth-first search (DFS) algorithm.
'''

def dfs(graph, start):
    visited = set() # To keep track of visited nodes
    stack = [start] #Stack for DFS

    while stack:
        node = stack.pop() # Pop the node from the stack
        if node not in visited:
            print(node) # Process the node (or add to result)
            visited.add(node)
            # Add neighbors of the node to the stack (unvisited nodes)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)


graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'],
    'E' : ['B', 'F'],
    'F' : ['E']
}

dfs(graph, 'A')