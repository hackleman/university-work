import sys

def display(board):
    for i in range(len(board)):
        for j in range(len(board)):
                sys.stdout.write(str(board[i][j]) + ' ')
        print('')

def isvalid(board, row, col):

    # check the same row for 1's
    for c in range(col):
        if board[row][c] == 1: return False
    # check diagonal for 1's
    for _i in range(len(board)):
        if row-_i >= 0 and col-_i >= 0:
            if board[row-_i][col-_i] == 1: return False
        if row+_i <= len(board)-1 and col-_i >= 0:
            if board[row+_i][col-_i] == 1: return False
    
    return True


def helper(board, col):
    global count

    if col == len(board):
        count += 1
        return

    for i in range(len(board)):
        
        if isvalid(board, i, col):

            board[i][col] = 1

            helper(board, col + 1)

            board[i][col] = 0

def nqueens(n):
    global count

    board = [[0 for i in range(n)] for i in range(n)]

    helper(board, 0)
    return count
    
count = 0
print(nqueens(5))
