"""

Create an algorithm that can verify if a sudoku board is valid.
Requirements:
- A row cannot have duplicated number otherwise return False
- A column cannot have duplicated number otherwise return False
- A sub box (3:3) cannot have duplicated number otherwise return False

Input: [[], [], []] Output: bool

Implementation:
- Go trough the matrix r, c 
- Check if matrix[r][c] exists in row[r]
- Check if matrix[r][c] exists in col[c]
- Check if matrix[r][c] exists in box[(r//3, c//3)]

- Add the value: 
- row[r] = row[r].append(matrix[r][c])
- col[c] = col[c].append(matrix[r][c])
- box[(r//3, c//3)] = box[(r//3, c//3)].append(matrix[r][c])

"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}

        for r in range(len(board)):
            for c in range(len(board[r])):
                box_index = (r//3, c//3)
                value = board[r][c]
                
                # Check if its a valid digit
                if value == ".":
                    continue

                # Add that value to the row
                if r in row:
                    if value in row[r]:
                        return False

                    row[r].append(value)
                else:
                    row[r] = [value]

                # Add that value to the row
                if c in col:
                    if value in col[c]:
                        return False

                    col[c].append(value)
                else:
                    col[c] = [value]

                # Add that value to the box
                if box_index in box:
                    if value in box[box_index]:
                        return False
                        
                    box[box_index].append(value)
                else:
                    box[box_index] = [value]


        return True