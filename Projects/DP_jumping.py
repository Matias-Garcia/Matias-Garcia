# Dynamic Programming Algorithm for Maximum Lilypad Score

def Fred(r, g, b):
    def dp(i, last_color, cache):
        # Base case: If Fred reaches or passes the end of the lilypad row
        if i >= len(r):
            return 0

        # Check if the result is already cached
        if cache[i][last_color] is not None:
            return cache[i][last_color]

        # Recursive case: Maximize the score by choosing a different color
        total_score = 0
        for color in range(3):  # Iterate through colors: 0 = red, 1 = green, 2 = blue
            if color != last_color:  # Fred cannot land on the same color twice in a row
                jump_score = 0
                if color == 0:  # Red
                    jump_score = r[i] + dp(i + 1, color, cache)
                elif color == 1:  # Green
                    jump_score = g[i] + dp(i + 1, color, cache)
                elif color == 2:  # Blue
                    jump_score = b[i] + dp(i + 1, color, cache)

                total_score = max(total_score, jump_score)

        # Cache the result to avoid redundant computations
        cache[i][last_color] = total_score
        return total_score

    # Initialize the cache: 2D array with dimensions [len(r)][3]
    cache = [[None] * 3 for _ in range(len(r))]

    # Start the recursion with no last color (-1)
    return dp(0, -1, cache)


# Test the function
r = [8, 1, 3, 2]
g = [2, 1, 1, 2]
b = [3, 1, 2, 7]

print(Fred(r, g, b))  # Expected Output: 19
