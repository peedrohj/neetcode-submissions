# Begin in image[sr][sc] and set it to color 
# Repeat for each pixel that has the same color

# [1,1,1]   [2,2,2]
# [1,1,0]   [2,2,0]
# [1,0,1]   [2,0,1]

# sr = 2, sc = 2, color = 2
# DFS 

class Solution:
    def __dfs(self, matrix: List[List[int]], row: int, col: int) -> List[List[int]]:
        MAX_ROW, MAX_COL = len(matrix), len(matrix[0])

        # Base return cases
        if min(row, col) < 0:
            return matrix

        if row == MAX_ROW or col == MAX_COL:
            return matrix

        if matrix[row][col] == self.color:
            return matrix

        if matrix[row][col] != self.start_color:
            return matrix

        # Solution
        if matrix[row][col] == self.start_color:
            matrix[row][col] = self.color

        # Go trough all possible paths
        self.__dfs(matrix=matrix, row=row-1, col=col)
        self.__dfs(matrix=matrix, row=row+1, col=col)
        self.__dfs(matrix=matrix, row=row, col=col-1)
        self.__dfs(matrix=matrix, row=row, col=col+1)

        return matrix
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.color = color
        self.start_color = image[sr][sc]

        return self.__dfs(matrix=image, row=sr, col=sc)