value = [0, 5, 10, 7, 9]
weight = [0, 2, 5, 3, 4]

capacity = 6
capacity += 1

# number of items
length = len(value)

tab = [[0 for i in range(capacity)] for j in range(length)]

for i in range(1, length):
	for v in range(capacity):
		new_value = 0
		# choose new
		if weight[i] <= v:
			new_value += value[i]
			new_value += tab[i - 1][v - weight[i]]

		old_value = tab[i - 1][v]
		tab[i][v] = max(old_value, new_value)

ans = []
new_capacity = capacity - 1
# iterate through all items in reverse order
# go fron n to 1
for i in range(length - 1, 0, -1):
	if tab[i][new_capacity] > tab[i-1][new_capacity]:
		ans.append(i)
		new_capacity -= weight[i]
		
print(ans)

#for el in tab:
#	print(el)
