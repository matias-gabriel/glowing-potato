def hasConflict(position, board):
    for i in board:
        if position[1] == i:
            return True

    diagonal = (position[0] - 1, position[1] - 1, position[1] + 1)

    while diagonal[0] > -1:
        if diagonal[1] > - 1 and board[diagonal[0]] == diagonal[1]:
            return True
        elif diagonal[2] < len(board) and board[diagonal[0]] == diagonal[2]:
            return True
        else:
            diagonal = (diagonal[0] - 1, diagonal[1] - 1, diagonal[2] + 1)

    return False

def calcNQueens(idx, board, n):
    if board[n-1] is not None:
        print(board)
        return 1

    result = 0

    for j in range(n):
        if not hasConflict((idx, j), board):
            board[idx] = j
            result+=calcNQueens(idx + 1, board, n)
            board[idx] = None

    return result
    
class Solution(object):
        
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = [None] * n

        return calcNQueens(0, board, n)
         