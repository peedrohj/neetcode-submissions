"""

Create an algorithm that can count the number of islands.
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

Requirements:
- An islands can be defined by a group of 1 surrounded by 0
- An island is formed by connecting adjacent nodes
- 1 = island
- 0 = water

Solution:
- For every island reach all the possible 1 and make it to 0 and increment the number of islands
"""

# 2D grid where 1 = land and 0 = water

# ROW = len(grid) COL = len(grid[0])
# visted_index = [[0] * COL for _ in range(ROW)]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        island = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return

            if grid[row][col] == "0":
                return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "0":
                    continue

                island += 1

                dfs(row, col)

        return island
