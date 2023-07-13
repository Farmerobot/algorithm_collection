import time
import random
import matplotlib.pyplot as plt

def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    for i in range(n+1):
        for w in range(capacity+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# List to store times and capacities
times = []
capacities = []

for capacity in range(10, 101, 10):  # Test for capacities 10, 20, ..., 100
    weights = [random.randint(1, 100) for _ in range(capacity)]
    values = [random.randint(1, 100) for _ in range(capacity)]

    start_time = time.time()
    knapsack(weights, values, capacity)
    end_time = time.time()

    times.append(end_time - start_time)
    capacities.append(capacity)

# Plot the results
plt.figure(figsize=(10,6))
plt.plot(capacities, times, marker='o')
plt.title('Execution Time of Knapsack Problem')
plt.xlabel('Capacity / Number of Items')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()

