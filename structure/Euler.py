from collections import defaultdict

adj = defaultdict(list)

vis = defaultdict(bool)

MAX = 1001
Euler = [0] * (2 * MAX)


def add_edge(u, v):
    adj[u].append(v)
    adj[v].append(u)


def eulerTree(u, index):
    vis[u] = True
    Euler[index] = u
    index += 1
    for nbr in adj[u]:
        if not vis[nbr]:
            index = eulerTree(nbr, index)
            Euler[index] = u
            index += 1
    return index


# Function to print Euler Tour of Tree
def printEulerTour(root, N):
    index = 0
    eulerTree(root, index)
    for i in range(2 * N - 1):
        print(Euler[i], end=" ")


# Driver Code
N = 4
add_edge(1, 2)
add_edge(2, 3)
add_edge(2, 4)

printEulerTour(1, N)
