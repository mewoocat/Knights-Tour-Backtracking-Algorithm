# Backtracking Project


# gets user input for size of chessboard
size = int(input("Enter chessboard size: "))
# gets user input for starting row
row = int(input("Enter starting row (0 indexed): "))
# gets user input for starting column
column = int(input("Enter starting column (0 indexed): "))

# intializes chessboard to size inputed
# source: https://www.adamsmith.haus/python/answers/how-to-initialize-a-2d-array-in-python
chessboard = [[ -1 for row in range(size)] for column in range(size)]

# the 8 possible moves for a knight
moves = [
    [-1, 2],
    [1, 2],
    [2, 1],
    [2, -1],
    [-1, -2],
    [1, -2],
    [-2, 1],
    [-2, -1]
]

# step counter for solution
count = -1

# solves knight's tour via backtracking
def knightsTour(count, size, row, column):

    # checks for valid position
    if (row >= 0 and row < size and column >= 0 and column < size and chessboard[row][column] == -1):

        # increment step counter
        count+=1

        # sets current position on chessboard
        chessboard[row][column] = count

         # return true if solution is found
        if (count == (size * size) - 1):
            return True

        # try moves
        for move in moves:
            if (knightsTour(count, size, row + move[0], column + move[1]) == True):
                return True

        # backtrack if no possible moves
        # resets position to empty
        chessboard[row][column] = -1
         # decrement step counter
        count-=1

        return False

    # if position is not valid
    else:
        return False


# prints chessboard
def printChessboard(chessboard):
    for row in chessboard:
        for column in row:
            print(f'{column:3}', end=" ")
        print()

# run knight's tour algorithm
if (knightsTour(count, size, row, column) == True):
    print("Solution found.")
    printChessboard(chessboard)
else:
    print("No solution...")
