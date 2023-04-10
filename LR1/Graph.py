class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}
        self.weights = {}
    
    def add_vertex(self,vertex):
        self.vertices.add(vertex)

    def add_edge(self, vertex1, vertex2, weight=1): 
        if self.is_edge(vertex1,vertex2):
            return
        else:
            self.add_vertex(vertex1)
            self.add_vertex(vertex2)
            self.edges.setdefault(vertex1, []).append(vertex2)
            self.edges.setdefault(vertex2, []).append(vertex1)
            self.weights[(vertex1, vertex2)] = weight
            self.weights[(vertex2, vertex1)] = weight
    
    def get_verticies_value(self):
        return len(self.vertices)
    
    def get_vertecies(self):
        return self.vertices

    def remove_edge(self, vertex1, vertex2):
        self.edges[vertex1].remove(vertex2)
        self.edges[vertex2].remove(vertex1)
        del self.weights[(vertex1, vertex2)]
        del self.weights[(vertex2, vertex1)]

    def is_edge(self, vertex1, vertex2):
        return vertex2 in self.edges.get(vertex1, [])

    def get_weight(self, vertex1, vertex2):
        return self.weights[(vertex1, vertex2)]

    def set_weight(self, vertex1, vertex2, weight):
        self.weights[(vertex1, vertex2)] = weight
        self.weights[(vertex2, vertex1)] = weight

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        
        if start_vertex == end_vertex:
            return [path]
        
        paths = []
        for neighbor in self.edges.get(start_vertex, []):
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        
        return paths

    def build_adjacency_matrix(self):
        vertices = list(self.vertices)
        matrix = [[0] * len(vertices) for _ in range(len(vertices))]
        for i, vertex1 in enumerate(vertices):
            for j, vertex2 in enumerate(vertices):
                if self.is_edge(vertex1, vertex2):
                    matrix[i][j] = self.get_weight(vertex1, vertex2)

        return matrix

    def print_adjacency_matrix(self):
        matrix = self.build_adjacency_matrix()
        for row in matrix:
            print(row)

    def __str__(self):
        result = ""
        for vertex in self.vertices:
            # Append the vertex and its edges to the result string
            result += f"{vertex}: "
            result += ", ".join(str(neighbor) + f"({self.weights[(vertex, neighbor)]})" for neighbor in self.edges.get(vertex, []))
            result += "\n"
        return result
    
