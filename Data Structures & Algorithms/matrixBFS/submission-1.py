# 0 = land 
# 1 = rocks 
# starting point = 0,0 
# success case = lenght(grid), lenght(grid[0])

# [0, 0, 0, 0]
# [1, 1, 0, 0]
# [0, 0, 0, 1]
# [0, 1, 0, 0]



class Solution:
    def __reach_the_end(self, row: int, col: int) -> bool:
        if row == self.MAX_ROW - 1 and col == self.MAX_COL - 1:
            return True
        
        return False

    def __search_node(self, grid: List[List[int]], row: int, col: int, queue: deque, visit: set) -> Tuple[deque, set]:
        print(f"row {row} - col: {col}")
        print("=====")

        
        if min(row, col) < 0:
            return queue, visit

        if row == self.MAX_ROW or col == self.MAX_COL:
            return queue, visit
        
        if (row, col) in visit:
            return queue, visit

        if grid[row][col] == 1:
            return queue, visit

        queue.append((row, col))
        visit.add((row, col))

        return queue, visit


    def __bfs(self, grid: List[List[int]]) -> int:
        visit = set()
        queue = deque()

        queue.append((0,0))
        visit.add((0,0))

        length = 0

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                if self.__reach_the_end(row=row, col=col):
                    return length

                queue, visit = self.__search_node(grid=grid, row=row+1, col=col, visit=visit, queue=queue)
                queue, visit = self.__search_node(grid=grid, row=row-1, col=col, visit=visit, queue=queue)
                queue, visit = self.__search_node(grid=grid, row=row, col=col+1, visit=visit, queue=queue)
                queue, visit = self.__search_node(grid=grid, row=row, col=col-1, visit=visit, queue=queue)

            length += 1


        return -1
    
    def shortestPath(self, grid: List[List[int]]) -> int:
        self.MAX_ROW, self.MAX_COL = len(grid), len(grid[0])

        return self.__bfs(grid=grid)