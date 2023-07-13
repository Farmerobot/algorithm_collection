import numpy as np

adj = [
	[],
	[2, 6],
	[2, 3],
	[4],
	[9, 5],
	[1],
	[7, 8],
	[],
	[7],
	[]
]

"""adj = [
	[1, 6],
	[6, 7],
	[6, 8],
	[7, 8],
	[1, 2],
	[2, 2],
	[2, 3],
	[3, 4],
	[4, 9],
	[4, 5],
	[5, 1],
]

n = np.amax(adj)
mat = np.zeros((n+1,n+1))

for x in adj:
	mat[x[0]-1][x[1]] = 1"""


def process(n):
	print(n)

def bfs(start):
	global adj
	 
	visited = [False] * len(adj)
	queue = []
	queue.append(start)
	visited[start] = True
	
	while (len(queue) > 0):
		vertex = queue.pop(0)
		process(vertex)
		for neighbour in adj[vertex]:
			if not visited[neighbour]:
				visited[neighbour] = True
				queue.append(neighbour)

visited = [False] * len(adj)

def dfs(vertex):
	global adj, visited
	
	if visited[vertex]:
		return
		
	visited[vertex] = True
	process(vertex)
	for neighbour in adj[vertex]:
		if not visited[neighbour]:
			dfs(neighbour)

dfs(1)
