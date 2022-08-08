import numpy as np
from networkx import connected_components
from numpy import VisibleDeprecationWarning


class ConnectedGraph():
    def __init__(self, V):
        # No. of vertices
        self.V = V
        # adjacency list
        self.adj = [[] for i in range(self.V)]

    def number_of_connect_components(self):
        visited = [False for i in range(self.V)]
        count = 0
        for v in range(self.V):
            if (visited[v] == False):
                self.dfs_utility(v, visited)
                count += 1
        return count

    def dfs_utility(self, temp, v, visited):
        visited[v] = True
        # recur for all vertices
        # adjecent to this vertex
        temp.append(v)
        for i in self.adj[v]:
            if visited[i] == False:
                temp = self.dfs_utility(temp, i, visited)
        return temp

    # add an undirected edge
    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def connect_component(self):
        visited = []
        conn_component = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                conn_component.append(self.dfs_utility(temp, v, visited))
                return conn_component


if __name__ == "__main__":
    g = ConnectedGraph(9)
    g.add_edge(5, 3)
    g.add_edge(3, 7)
    g.add_edge(3, 0)
    g.add_edge(0, 4)
    g.add_edge(4, 8)
    g.add_edge(2, 0)
    g.add_edge(6, 1)
    connected_components = g.connect_component()
    print(connected_components)
"""
doc file kiem tra do thi co huong va do thi vo huong
tao list bang nhan 9 dinh
ham sothanhphanlienthong 
for i in range(dinh):
 if nhan[i] == 0:
 bien so thanh phan lien thong += 1
 nhan[i] = sothanhphanlienthong
 -> viet ham de quy tim cac dinh lien thong(do thi, bang nhan, dinh: int):
 for (i, len())..
 

"""