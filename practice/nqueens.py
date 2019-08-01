def display(board):
    for _row in range(len(board)):
        print('')
        for _column in range(len(board)):
            print(board[_row][_column], end = ' ')

# def nocollisions(row, col, board):
#     board[row][col] = 0
#     # scan row
#     for _row in range(len(board)):
#         if board[_row][col] == 1: return False
            
#     # scan column
#     for _col in range(len(board)):
#         if board[row][_col] == 1: return False

#     board[row][col] = 1
#     # scan diagonal
#     if (not scandiagonals(row, col, board)): return False
    
#     return True

# def scandiagonals(row, col, board):
#     for _i in range(1, len(board)):
#         if (row - _i >= 0 and col - _i >= 0):
#             if board[row-_i][col-_i] == 1: return False
#         if (row + _i < len(board) and col + _i < len(board)):
#             if board[row+_i][col+_i] == 1: return False
#         if (row - _i >= 0 and col + _i < len(board)):
#             if board[row-_i][col+_i] == 1: return False
#         if (row + _i < len(board) and col - _i >= 0):
#             if board[row+_i][col-_i] == 1: return False
#     return True

def isSafe(board, row, col):

    for i in range(col):
        if board[row][i] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def nqueens(board, col, count):

    if col == 8:
        display(board)
        count[0] += 1
        return
        
    # place and mark starting with first available 
    for i in range(8):

        if isSafe(board, i, col):

            board[i][col] = 1

            nqueens(board, col + 1, count)
                
            board[i][col] = 0

    
count = [0]
board = [ [ 0 for i in range(8) ] for j in range(8) ]

nqueens(board, 0, count)
print(count[0])