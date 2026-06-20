# BFS - what is the short path?

# [1,0,0]
# [1,1,0]
# [1,1,0]


class Solution:
    def __reach_the_end(self, row: int, col: int) -> bool:
        return row == self.MAX_ROW - 1 and col == self.MAX_COL - 1

    def __is_valid(self, grid: List[List[int]], row: int, col: int, visit: set) -> bool:

        if min(row, col) < 0:
            return False

        if row >= self.MAX_ROW or col >= self.MAX_COL:
            return False

        if grid[row][col] == 1:
            return False

        if (row, col) in visit:
            return False

        return True

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.MAX_ROW, self.MAX_COL = len(grid), len(grid[0])

        queue = deque()
        visit = set()

        if not self.__is_valid(grid=grid, row=0, col=0, visit=visit):
            return -1

        queue.append((0, 0))
        visit.add((0, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        length = 1

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if self.__reach_the_end(row=row, col=col):
                    return length

                for dir_r, dir_c in directions:
                    new_row, new_col = row + dir_r, col + dir_c

                    if self.__is_valid(grid=grid, row=new_row, col=new_col, visit=visit):
                        queue.append((new_row, new_col))
                        visit.add((new_row, new_col))

            length += 1

        return -1
