class Graph:
    def __init__(self) -> None:
        self.vertices = {}

    def add_vertex(self,vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    def remove_vertex(self,vertex):
        if vertex in self.vertices:
            adjacent_vertices = self.vertices[vertex]
            del self.vertices[vertex]
            for v in adjacent_vertices:
                self.vertices[v].remove(vertex)

    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].remove(vertex2)
            self.vertices[vertex2].remove(vertex1)
    
    def get_adjacent_vertices(self,vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        return []
    
    def display(self):
        for vertex in self.vertices:
            print(vertex,"->",self.vertices[vertex])


# Now Testing :

# Create an instance of the graph
graph = Graph()

# Add vertices to the graph
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

# Add edges to the graph
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')
graph.add_edge('E', 'A')

# Display the graph
graph.display()
print("\n")
# Output:
# A -> ['B', 'E']
# B -> ['A', 'C']
# C -> ['B', 'D']
# D -> ['C', 'E']
# E -> ['D', 'A']

# Remove a vertex and its associated edges from the graph
graph.remove_vertex('C')

# Display the graph after removing a vertex
graph.display()
print("\n")
# Output:
# A -> ['B', 'E']
# B -> ['A']
# D -> ['E']
# E -> ['D', 'A']

# Get the adjacent vertices of a specific vertex
adjacent_vertices = graph.get_adjacent_vertices('B')
print(adjacent_vertices)
# Output: ['A']

# Remove an edge between two vertices
graph.remove_edge('A', 'E')

# Display the graph after removing an edge
graph.display()
print("\n")
# Output:
# A -> ['B']
# B -> ['A']
# D -> ['E']
# E -> ['D']
