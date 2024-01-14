# The Knapsack Problem
The knapsack problem is a classic example in computer science, used to illustrate various problem-solving approaches including recursion and dynamic programming.

## Let's start with the recursive solution. 

The idea behind the recursive approach is to consider all subsets of items and calculate the total weight and value of each subset. We only consider subsets whose total weight is within the capacity of the knapsack. For each item, we can either include it in the knapsack or exclude it. This creates a binary tree of possibilities, which we explore recursively.

## Here's a basic outline of the recursive function: 

### Base Case:

If we have no items left or the capacity of the knapsack is 0, the maximum value we can obtain is 0.

### Case 1 - Include the Item: 

If the item's weight is less than or equal to the knapsack's capacity, include it and proceed to the next item with reduced capacity.

### Case 2 - Exclude the Item: 

Skip the item and proceed to the next item with the same capacity.

### Return the Maximum Value: 

For each item, we take the maximum of these two cases.


## Let's move on to the dynamic programming solution. 
The dynamic programming approach to the knapsack problem is much more efficient than the recursive approach, as it avoids recomputation of the same subproblems. This is achieved by storing the results of subproblems in a table.

Here's how you can implement the dynamic programming solution in Python:

### Create a 2D Array: 

The array dp is used to store the maximum value that can be attained with the given weight. The size of dp will be (n+1) x (capacity+1) where n is the number of items.

### Initialize the Table: 

Initialize the first row and first column as 0, as the maximum value with 0 items or 0 capacity is 0.

### Fill the Table: 

For each item, go through all weights from 1 to capacity and fill the table according to the following rule:

    If the item's weight is less than or equal to the current weight limit, set dp[i][w] as the maximum of two values:
        The value of the current item plus the value of the remaining capacity (values[i-1] + dp[i-1][w-weights[i-1]]).
        The value without including the current item (dp[i-1][w]).
    Otherwise, the value is the same as without the current item.
### Return the Result: 

The bottom-right corner of the table will hold the maximum value that can be carried in the knapsack.