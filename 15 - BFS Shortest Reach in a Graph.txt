class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = {}
        self.edge_weight = 6
        for i in range(n):
            self.edges[i] = []
    def connect(self, x, y):
        # self.edges.setdefault(x, [])
        self.edges[x].append(y)
        # self.edges.setdefault(y, [])
        self.edges[y].append(x)
    def find_all_distances(self, s):
        distances = [-1] * self.n
        distances[s] = 0
        pointer = 0
        connected_nodes = [s]
        while (pointer < len(connected_nodes)):
            for node in self.edges[connected_nodes[pointer]]:
                if (connected_nodes.count(node) == 0):
                    connected_nodes.append(node)
                    distances[node] = distances[connected_nodes[pointer]] + 1
            pointer += 1
        distances.pop(s)
        distances = [a * 6 if a != -1 else -1 for a in distances]
        print(' '.join([str(a) for a in distances]))

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)
    
