def fractional_knapsack():
    num_items = int(input("Enter the number of items: "))
    weights = []
    values = []

    # Input weights and values for each item
    for i in range(num_items):
        weight = float(input(f"Enter the weight of item {i + 1}: "))
        value = float(input(f"Enter the value of item {i + 1}: "))
        weights.append(weight)
        values.append(value)

    capacity = float(input("Enter the capacity of the knapsack: "))
    res = 0.0

    # Create a list of items with their value-to-weight ratio
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(num_items)]
    
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0], reverse=True)

    # Iterate through the sorted items
    for ratio, weight, value in items:
        if capacity <= 0:  # Capacity completed - Bag fully filled
            break
        if weight > capacity:  # Current item's weight exceeds available capacity
            res += capacity * ratio  # Take the fraction of the item that fits
            capacity = 0
        else:  # Take the whole item
            res += value
            capacity -= weight

    print(f"Maximum value in the knapsack: ", res)

fractional_knapsack()

# Test Case:
# Number of items: 4
# Weights: 10, 20, 30, 5
# Values: 60, 100, 120, 30
# Capacity of the knapsack: 50
# Expected output: Maximum value in the knapsack: 240.00

    """
    Fractional Knapsack Problem:
    The goal is to maximize the total value of items in a knapsack with a fixed capacity.
    Unlike the 0/1 knapsack problem, items can be divided, allowing for fractional amounts.

    Greedy Approach:
    1. Calculate value-to-weight ratio (r_i = v_i / w_i) for each item.
    2. Sort items in descending order based on their ratio.
    3. Iterate through the sorted items:
       - If an item can fit entirely, take it.
       - If not, take the fraction that fits.
    4. Continue until the knapsack is full or all items have been considered.

    Example:
    Items: [(Weight, Value)]
    - (10, 60), (20, 100), (30, 120)
    Capacity: 50
    - Total Value: 240.00 (Take full Item 1 and Item 2, and 2/3 of Item 3)

    How the Code Uses the Greedy Approach:
    - It calculates the value-to-weight ratio for each item to prioritize items with higher value per weight.
    - Items are sorted based on this ratio.
    - The algorithm selects items greedily, taking full items when possible and fractions of items when the knapsack is near capacity.
    """
