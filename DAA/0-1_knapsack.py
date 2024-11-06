def solve_knapsack():
    # Input the number of items
    num_items = int(input("Enter the number of items: "))
    val = []  # List to store values of items
    wt = []   # List to store weights of items

    # Input values and weights for each item
    for i in range(num_items):
        value = int(input(f"Enter the value of item {i + 1}: "))
        weight = int(input(f"Enter the weight of item {i + 1}: "))
        val.append(value)
        wt.append(weight)

    # Input the maximum capacity of the knapsack
    W = int(input("Enter the capacity of the knapsack: "))

    def knapsack(W, n):
        # Create a 2D array to store the maximum value for each (n, W) combination
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        # Fill the dp array using a bottom-up approach
        for i in range(1, n + 1):
            for w in range(1, W + 1):
                # If the item's weight is less than or equal to the capacity
                if wt[i - 1] <= w:
                    # Choose the maximum between including the item or excluding it
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt[i - 1]] + val[i - 1])
                else:
                    # If the item's weight is more, we can't include it
                    dp[i][w] = dp[i - 1][w]

        # The maximum value is found in the bottom-right cell of the dp table
        return dp[n][W]

    # Calculate the maximum value and print it
    max_value = knapsack(W, num_items)
    print(f"The maximum value that can be obtained is: {max_value}")

solve_knapsack()




    """
    0-1 Knapsack Problem:
    The goal is to maximize the total value of items in a knapsack with a fixed capacity.
    Each item can either be taken in full or left behind; partial items cannot be taken.

    Dynamic Programming Approach:
    1. Create a 2D table (dp) where dp[i][w] represents the maximum value that can be obtained
       with the first i items and a maximum weight w.
    2. Initialize the table such that dp[0][w] = 0 for all w (no items means no value).
    3. Iterate through each item and each capacity:
       - If the item's weight is less than or equal to the current capacity, consider including it.
       - Otherwise, retain the value from the previous item.
    4. The solution to the problem is found in the bottom-right cell of the table (dp[n][W]).

    Example:
    Items: [(Weight, Value)]
    - (2, 3), (3, 4), (4, 5), (5, 6)
    Capacity: 5
    - Total Value: 7.00 (Take Item 1 and Item 2)

    How the Code Implements the Dynamic Programming Approach:
    - It initializes a 2D array to store maximum values.
    - The nested loops fill this array based on whether each item can fit within the capacity.
    - The maximum achievable value for the full set of items and the given capacity is extracted from the table.
    """
