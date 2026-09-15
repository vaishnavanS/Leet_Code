class Solution(object):
    def exist(self, board, word):
        def back(x,y,c):
            if x<0 or y<0 or x>= len(board) or y>=len(board[0]):
                return False
            if board[x][y] != word[c]:
                return False
            if c == len(word)-1:
                return True
            temp = board[x][y]
            board[x][y] = "$"
            if back(x+1,y,c+1):
                board[x][y] = temp
                return True
            if back(x,y+1,c+1):
                board[x][y] = temp
                return True
            if back(x-1,y,c+1):
                board[x][y] = temp
                return True
            if back(x,y-1,c+1):
                board[x][y] = temp
                return True
            board[x][y] = temp
            return False
        for x in range(len(board)):
            for y in range(len(board[0])):
                if back(x,y,0):
                    return True
                    break
        return False