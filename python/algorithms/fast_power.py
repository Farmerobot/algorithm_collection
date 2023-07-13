a = 5
b = 13

c = [
	[1, 1],
	[1, 0]
]

test = [
	[1, 2],
	[3, 4],
]

def power(base, power):
	res = 1
	while power > 0:
		if power % 2 == 1:
			res *= base
		base *= base
		power //= 2
	return res

def matrix_multiply(a, b):
	width = len(b)
	height = len(a[0])
	res = [[0 for x in range(height)] for y in range(width)]
	
	for x in range(width):
		for y in range(height):
			for i in range(len(a)):
				res[x][y] += a[x][i] * b[i][y]
				
	return res

def matrix_power(base, power):
	width = len(base)
	height = len(base[0])
	if width != height:
		print("can't square a non-square matrix")
		return
	res = [[0 for x in range(width)] for y in range(width)]
	for x in range(width):
		res[x][x] = 1
	while power > 0:
		if power % 2 == 1:
			res = matrix_multiply(res, base)
		base = matrix_multiply(base, base)
		power //= 2
	return res

def fib(n):
	if n == 1:
		return 0
	mat = [
		[1, 1],
		[1, 0]
	]
	res = matrix_power(mat, n-2)
	return res[1][1] + res[1][0]

#print(matrix_multiply(test, test))
#print(matrix_power(test, 3))
for x in range(20):
	x += 1
	print(f"{x}th fibonacci number: {fib(x)}")
#print("default: ", 5**13)
#print("custom:  ", power(5,13))
