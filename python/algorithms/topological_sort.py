from copy import deepcopy

dag = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0, 1],
    5: [0, 2],
}

dag_matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
]

def dfs(vertex, adj, stack, visited):
    if visited[vertex]:
        return
    
    visited[vertex] = True
    for neighbour in adj[vertex]:
        if not visited[neighbour]:
            dfs(neighbour, adj, stack, visited)
    stack.append(vertex)

def topological_sort(adj):
    n = len(adj)
    visited = [False] * n
    available = [True] * n
    stack = []

    for key, value in adj.items():
        for x in value:
            available[x] = False

    for key, val in enumerate(available):
        if val:
            dfs(key, adj, stack, visited)

    return stack[::-1]

def dfs_mat(vertex, mat, stack, visited):
    if visited[vertex]:
        return
    
    visited[vertex] = True

    for neighbour, value in enumerate(mat[vertex]):
        if not value:
            continue
        if visited[neighbour]:
            continue
        dfs_mat(neighbour, mat, stack, visited)
    
    stack.append(vertex)

def topological_sort_mat(mat):
    n = len(mat)
    visited = [False] * n
    available = [True] * n
    stack = []

    for y in mat:
        for key, x in enumerate(y):
            if x == 1:
                available[key] = False
    
    for x, val in enumerate(available):
        if val:
            dfs_mat(x, mat, stack, visited)

    return stack[::-1]

def topological_sort_naive_(_adj):
    adj = deepcopy(_adj)
    n = len(adj)
    stack = []
    available = {x: True for x in range(n)}
    while True:
        for key, y in adj.items():
            for x in y:
                available[x] = False
        print(available)
        # Check if there are any more free nodes
        changed = False
        for key, x in enumerate(available):
            if not x:
                continue
            changed = True
            stack.append(key)
            del(adj[key])
            del(available[key])
        # No more nodes to traverse; exit
        if not changed:
            break
    return stack[::-1]

def topological_sort_naive(graph):
    # create a dictionary to store the in-degree of each vertex
    in_degree = {v: 0 for v in dag}
    
    # calculate the in-degree of each vertex
    for v in dag:
        for neighbor in dag[v]:
            in_degree[neighbor] += 1
    
    # initialize an empty list to store the sorted vertices
    sorted_vertices = []
    
    # iterate over all vertices, print and remove those "available"
    # (having no input arcs) until all vertices are printed
    while len(sorted_vertices) < len(dag):
        available_vertices = [v for v in dag if in_degree[v] == 0 and v not in sorted_vertices]
        if not available_vertices:
            raise ValueError("Input graph is not a DAG")
        for v in available_vertices:
            print(v)
            sorted_vertices.append(v)
            for neighbor in dag[v]:
                in_degree[neighbor] -= 1
    return sorted_vertices

# print(topological_sort_mat(dag_matrix))
# print(topological_sort(dag))
print(topological_sort_naive(dag))