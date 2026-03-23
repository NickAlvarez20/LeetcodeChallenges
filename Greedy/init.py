# Greedy algorithms make a series of local best choices. The optimal solution to the entire problem contains within it the optimal solutions to its subproblems.
# look for keywords like minimum, maximum, shortest, or largest.
# Most leetcode greedy problems fall into these categories: 1. Sorting based (sort th einput by a specific criteria before processing) 2. Intervals - sort by end times to fit the most non-overlapping intervals. 3. Reachability - track the farthest point you can reach at any moment. 4. Greedy simulation - sim the process making the best choice at each step (e.g., giving change)

# Basic implementation -- Getting good
# Coin Change Problem - Make change for a specific amount using the min num of coins possible. The "greedy" strat is to always pick the largest possible coin that is less than or equal to the remaining amount.

def greedy_coin_change(amount, coins):
    # 1. Sort coins in descending order (largest first)
    coins.sort(reverse=True)

    result = []
    for coin in coins:
        # 2. Keep taking the current largest coin while it fits
        while amount >= coin:
            amount -= coin
            result.append(coin)

    return result


# Example Usage
available_coins = [1, 2, 5]
target_amount = 18
change = greedy_coin_change(target_amount, available_coins)

print(f"Coins used: {change}")
print(f"Total coins: {len(change)}")
