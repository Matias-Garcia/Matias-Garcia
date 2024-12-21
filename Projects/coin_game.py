# Complexity O(n^2)
# it does recursively calls itself with smaller subproblems, resulting in a time complexity of O(n^2) where n is the number of coins in the input list.
class Game:
    def __init__(self, coins):
        self.coins = coins
        # Create a 2D array to cache results of subproblems
        self.cache = [[(None, 0, True) for i in range(len(coins))] for j in range(len(coins))] # Create a 2D array because it's the best based on lecture
    
    def run(self, start, end):
        max_win = 0
        margin = 0
        takeRight = True
        
        # Base cases:
        # - If the list of coins is empty, return 0 coins won - CG([]) = 0
        # - If the start index is greater than the end index, return 0 coins won
        if self.coins == [] or start > end:  # Base case for empty list                                
            return (0, 0, takeRight)

        # Base case: If only one coin left, return that coin as the win - 𝐶𝐺 (𝑖, j) = 𝑐𝑖
        if start == end:                                                         # Base case for a single coin
            return (self.coins[start], self.coins[start], takeRight)           
        
        # If the result for the current range is already cached, return it
        if self.cache[start][end][0] is not None:                           # Check if result is cached
            return (self.cache[start][end][0], self.cache[start][end][1], self.cache[start][end][2])
        
        # Recursive formula:
        # CG([0 ... n − 1]) = max {left, right},
        # where
        # left = min {CG[1 ... n − 2], [CG 2 ... n − 1]} + coins[0]
        # right = min {CG[0 ... n − 3], [CG 1 ... n − 2]} + coins[n−1]
        left = min(self.run(start + 2, end)[0], self.run(start + 1, end - 1)[0])
        right = min(self.run(start + 1, end - 1)[0], self.run(start, end - 2)[0])

        # Decide the best option
        if self.coins[start] + left > self.coins[end] + right: #CG([0 ... n − 1]) = max {left, right}
            takeRight = False
            max_win = self.coins[start] + left
            player2 = self.run(start + 1, end)[0]
        else:
            takeRight = True
            max_win = self.coins[end] + right
            player2 = self.run(start, end - 1)[0]

        # Calculate the margin of victory
        margin = max_win - player2
        # Cache the result for future use
        self.cache[start][end] = (max_win, margin, takeRight)
        
        return (max_win, margin, takeRight)