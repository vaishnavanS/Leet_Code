class Solution(object):
    def uniquePathsIII(self, grid):
        row = len(grid)
        cols = len(grid[0])
        e = 0
        for i in range(row):
            for j in range(cols):
                if grid[i][j] != -1:
                    e += 1
                if grid[i][j] == 1:
                    sr = i
                    sc = j
        def dfs(r,c,rem):
            if r<0 or r>=row or c<0 or c>=cols:
                return False
            if grid[r][c] == -1:
                return False
            if grid[r][c] == 2:
                if rem == 1:
                    return True
                return False
            temp = grid[r][c]
            grid[r][c] = -1
            p = 0
            p += dfs(r+1,c,rem-1)
            p += dfs(r-1,c,rem-1)
            p += dfs(r,c+1,rem-1)
            p += dfs(r,c-1,rem-1)
            grid[r][c] = temp
            return p
        return dfs(sr,sc,e)
        