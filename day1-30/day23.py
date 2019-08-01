"""
You are given an M by N matrix consisting 
of booleans that represents a board. 
Each True boolean represents a wall. 
Each False boolean represents a tile 
you can walk on.

Given this matrix, a start coordinate,
 and an end coordinate, return the minimum
  number of steps required to reach the end 
  coordinate from the start. If there is no 
  possible path, then return null. You can move 
  up, left, down, and right. You cannot move through walls.
   You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), 
the minimum number of steps required to reach the end is 7, 
since we would need to go through (1, 2) because there is a 
wall everywhere else on the second row.
"""
board = []
traversed = []
start = (3, 0)
end = (0, 0)

def initialize():
    
    row1 = [0, 0, 0, 0]
    row2 = [1, 1, 0, 1]
    row3 = [0, 0, 0, 0]
    row4 = [0, 0, 0, 0]

    board.append(row1)
    board.append(row2)
    board.append(row3)
    board.append(row4)

    board[start[0]][start[1]] = -1

def mark(i, j, board, iteration):

    # mark top
    if i != 0 and board[i-1][j] == 0:
        board[i-1][j] = -1
        traversed.append([(i-1, j), iteration])
    # mark left
    if j != 0 and board[i][j-1] == 0:
        board[i][j-1] = -1
        traversed.append([(i, j-1), iteration])
    # mark right
    if j != (len(board)-1) and board[i][j+1] == 0:
        board[i][j+1] = -1
        traversed.append([(i, j+1), iteration])
    # mark bottom
    if i != (len(board)-1) and board[i+1][j] == 0:
        board[i+1][j] = -1
        traversed.append([(i+1, j), iteration])

def traverse():

    iteration = 1
    temp = []
    
    while(end not in temp):

        temp = []

        if iteration == 1: mark(start[0], start[1], board, 1)

        for y in traversed:
            if y[1] == iteration-1:
                temp.append(y[0])
        for x in temp:
            mark(x[0], x[1], board, iteration)

        iteration += 1

initialize()
traverse()

print(traversed[-1][-1])