class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        dist = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        def __add_room(row, col):
            if (
                row < 0
                or row == ROWS
                or col < 0
                or col == COLS
                or (row, col) in visit
                or grid[row][col] == -1
            ):
                return

            q.append([row, col])
            visit.add((row, col))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                __add_room(r + 1, c)
                __add_room(r - 1, c)
                __add_room(r, c + 1)
                __add_room(r, c - 1)

            dist += 1

