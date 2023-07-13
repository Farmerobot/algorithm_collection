import subprocess
import time
import matplotlib.pyplot as plt

# n - number of vertices
def generate_graph(vertices, edges):
    process = subprocess.Popen(['./graph.out', str(vertices), str(edges)], stdout=subprocess.PIPE)
    output, _ = process.communicate()

    lines = output.decode().splitlines()
    v, e = map(int, lines[0].split())
    # matrix
    adj = [[0 for i in range(v+1)] for j in range(v+1)]
    
    for line in lines[1:]:
        vi, vj = map(int, line.split())
        adj[vi][vj] = 1
        adj[vj][vi] = 1

    return adj

# n - number of vertices
def generate_hamiltonian_graph(vertices, edges):
    process = subprocess.Popen(['./hamilton.out', str(vertices), str(edges)], stdout=subprocess.PIPE)
    output, _ = process.communicate()

    lines = output.decode().splitlines()
    v, e = map(int, lines[0].split())
    # matrix
    adj = [[0 for i in range(v+1)] for j in range(v+1)]

    for line in lines[1:]:
        vi, vj = map(int, line.split())
        adj[vi][vj] = 1
        adj[vj][vi] = 1

    return adj

def recursive_hamiltonian_backtrack(adj, pos, stack):
    # dead end or cycle
    if pos == len(adj) - 1:
        return adj[stack[pos-1]][stack[0]] == 1

    # for each edge
    for i, x in enumerate(adj[stack[pos-1]]):
        # remove edge
        if x == 1 and i not in stack:
            stack[pos] = i
            if (recursive_hamiltonian_backtrack(adj, pos + 1, stack)):
                return True
            else:
                stack[pos] = -1
    return False

def generate_hamiltonian_cycle(vertices, edges, adj = None):
    if adj == None:
        adj = generate_hamiltonian_graph(vertices, edges)
    start_vertex = None
    # find start
    for i, x in enumerate(adj):
        edges = sum(x)
        # select first non-empty vertex
        if edges > 0:
            start_vertex = i
            break

    # for x in adj[1:]:
    #     print(x[1:])
    path_stack = [-1 for x in range(vertices)]
    path_stack[0] = start_vertex

    if (recursive_hamiltonian_backtrack(adj, 1, path_stack)):
        return path_stack
    else:
        return False

# n - number of vertices
def generate_eulerian_graph(n):
    process = subprocess.Popen(['./euler.out', str(n)], stdout=subprocess.PIPE)
    output, _ = process.communicate()

    lines = output.decode().splitlines()
    v, e = map(int, lines[0].split())
    # matrix
    adj = [[0 for j in range(v+1)] for i in range(v+1)]

    for line in lines[1:]:
        vi, vj = map(int, line.split())
        adj[vi][vj] = 1
        adj[vj][vi] = 1

    return adj

def recursive_eulerian_backtrack(adj, v, stack, start):
    stack.append(v)
    # dead end or cycle
    if sum(adj[v]) == 0:
        if v == start:
            return stack
        else:
            stack.pop()
            return

    # for each edge
    for i, x in enumerate(adj[v]):
        # remove edge
        if x == 1:
            adj[v][i] = 0
            adj[i][v] = 0
            recursive_eulerian_backtrack(adj, i, stack, start)

def generate_eulerian_cycle(n, adj=None):
    if adj == None:
        adj = generate_eulerian_graph(n)
    start_vertex = None
    # check if cycle exists; assume the graph is connected
    for i, x in enumerate(adj):
        edges = sum(x)
        # odd degree
        if edges % 2 != 0:
            return False
        # select first non-empty vertex
        if start_vertex == None and edges > 0:
            start_vertex = i

    # for x in adj[1:]:
    #     print(x[1:])
    path_stack = []
    recursive_eulerian_backtrack(adj, start_vertex, path_stack, start_vertex);

    return path_stack

def measure_execution_time(func, v, e, adj = None):
    start_time = time.process_time()
    func(v, e, adj)
    return (time.process_time() - start_time)

def measure_execution_time_euler(func, v, adj=None):
    start_time = time.process_time()
    func(v, adj)
    return (time.process_time() - start_time)

eulerian_times = []
hamiltonian_times = []
v_values = range(6, 30, 2)

def plot():
    global eulerian_times, hamiltonian_times, v_values
    plt.figure(figsize=(10, 5))

    plt.plot(v_values, eulerian_times, marker='o', label='Eulerian Cycle')
    plt.plot(v_values, hamiltonian_times, marker='o', label='Hamiltonian Cycle')

    plt.xlabel('Number of vertices (v)')
    plt.ylabel('Execution time (nanoseconds)')

    plt.yscale("log")

    plt.title('Execution times of Eulerian and Hamiltonian cycle algorithms')
    plt.legend()

    plt.show()

# for v in v_values:
#     eulerian_times.append(measure_execution_time_euler(generate_eulerian_cycle, v))
#     hamiltonian_times.append(measure_execution_time(generate_hamiltonian_cycle, v, 2 * v + 2))

# plot()

# for v in v_values:
#     eulerian_times.append(measure_execution_time_euler(generate_eulerian_cycle, v, generate_graph(v, v * 2 + 2)))
#     hamiltonian_times.append(measure_execution_time(generate_hamiltonian_cycle, v, v * 2 + 2, generate_graph(v, v * 2 + 2)))

# plot()

# print(eulerian_times)
# print(hamiltonian_times)

