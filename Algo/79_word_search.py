class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def sol(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            c = board[i][j]
            board[i][j] = ''
            f = False
            for row, column in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
                f |= sol(row, column, k + 1)
            board[i][j] = c
            return f
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if sol(i, j, 0):
                    return True
        return False
