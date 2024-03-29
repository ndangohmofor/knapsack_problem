def knapsack_recursive(capacity, weights, values, n):
    # Base case: No items left or no capacity in the knapsack
    if n == 0 or capacity == 0:
        return 0

    # If weight of the nth item is more than the knapsack capacity, then this item cannot be included
    if weights[n - 1] > capacity:
        return knapsack_recursive(capacity, weights, values, n - 1)

    # Return th max of two cases:
    # nth item included
    # nth item not included

    else:
        included = values[n - 1] + knapsack_recursive(capacity - weights[n - 1], weights, values, n - 1)
        excluded = knapsack_recursive(capacity, weights, values, n - 1)
        return max(included, excluded)


def knapsack_dp(capacity, weights, values, n):
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


# Example usage
values1 = [60, 100, 120]  # Values of the items
weights1 = [10, 20, 30]  # Weights of the items
capacity1 = 50  # Capacity of the knapsack
n1 = len(values1)  # Number of items

values2 = [250, 300, 500]
weights2 = [1, 3, 5]
capacity2 = 5
n2 = len(values2)

print(knapsack_recursive(capacity2, weights2, values2, n2))
print(knapsack_dp(capacity2, weights2, values2, n2))
