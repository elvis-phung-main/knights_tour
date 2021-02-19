# Determine a valid path for the knight to travel on an nxn grid
# Return 2D lists that includes integers representing the order
# of moves the knight went and the number of possible solutions

# The knight cannot ever travel on a space that it has already travelled on
# else it is invalid



# b - the board
# curr_x - the current x position of the knight 
# curr_y - the current y position of the knight
def solve(b, curr_x, curr_y, count):
    # once len(b) squared steps are made, the whole board has been traversed
    if count == len(b)**2:
        return True

    moves = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]] # represents the moves the knight can make
    
    for i in range(len(moves)):
        if isOnBoard(b, (curr_x + moves[i][0], curr_y + moves[i][1], count)):
            if b[curr_x + moves[i][0]][curr_y + moves[i][1]] == -1: # check if already traversed
                b[curr_x + moves[i][0]][curr_y + moves[i][1]] = count

                # Keep checking for possible solutions at the next positions
                if solve(b, curr_x + moves[i][0], curr_y + moves[i][1], count+1):
                    return True

                b[curr_x + moves[i][0]][curr_y + moves[i][1]] = -1 # backtrack and reset to -1 if solution cant be made
    
    # no solution could be found from all the possible moves in the path
    return False

# b - the board
# pos - the current position (x, y)
# Check if at least there is at least one valid move from the given position
# return True if there is at least one valid move, return False otherwise
def isOnBoard(b, pos): # check if the given coordinates (x,y) are in the board. Return True if so, return False if outside of the board
    if pos[0] < 0 or pos[0] >= len(b) or pos[1] < 0 or pos[1] >= len(b):
        return False
    return True

# function to print the board
def printBoard(b):
    for i in range(len(b)):
        for j in range(len(b)):
            print(b[i][j], end = " ")
        print()
    print()

# a chess board, 0s represent empty spaces
size = 6
board = [size*[-1] for i in range(size)]

start_x = 0
start_y = 0
board[start_x][start_y] = 0
printBoard(board)
print("")
print("")

print(solve(board,start_x,start_y,1))
printBoard(board)