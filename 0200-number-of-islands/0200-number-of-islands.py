class Solution(object):
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        count = 0
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m:
                return
            if grid[x][y] == "0":
                return
            grid[x][y] = "0"
            dfs(x, y+1)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x-1, y)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count