class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        def dfs(grid: List[List[int]], row: int, col: int, visit):
            possibilities = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            count = 0

            # Base cases
            if min(row, col) < 0 or row == len(grid) or col == len(grid[0]):
                return 0

            if (row, col) in visit:
                return 0

            if grid[row][col] == 1:
                return 0

            # Success case
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return 1

            visit.add((row, col))

            for dr, dc in possibilities:
                new_row = row + dr
                new_col = col + dc
                count += dfs(grid=grid, row=new_row, col=new_col, visit=visit)

            visit.remove((row, col))

            return count

        return dfs(grid=grid, row=0, col=0, visit=set())
