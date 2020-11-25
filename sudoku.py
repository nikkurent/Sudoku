board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

# Print a better looking version of sudoku board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - -')

        for j in range(len(board[0])):
            if j % 3 == 0:
                print("|", end="")

            if j == 8:
                print(str(board[i][j]) + "|")
            else:
                print(str(board[i][j]) + " ", end="")
                

# Retruns tuple --> (row, col) of every element that is equal to 0
def find_zero(board):
    for row in range(len(board)): #row
        for col in range(len(board[0])): #col
            if board[row][col] == 0:
                return (row, col) 
    return None

        
# Returns True if a given number can be placed in a given position
def is_valid(board, number, position):
    # Returns False if given number is repeated in a row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Returns False if given number is repeated in a column
    for i in range(len(board[0])):    
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Checks in what square is Zero
    square_x = position[0] // 3
    square_y = position[1] // 3

    # Returns False if given number is repeated in a box
    for i in range(square_x*3, square_x*3 + 3): 
        for j in range(square_y*3, square_y*3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True


# Backtracking algoritem to solve sudoku
def solve(board):
    find = find_zero(board)
    if not find:
        return True
    else:
        row, col = find
    
    # takes number between 1 and 9 and tries if is valid in is_valid() function
    for number in range(1, 10):
        # if is_valid == True --> place number in board
        if is_valid(board, number, (row,col)): 
            board[row][col] = number

            # Retruns True is board is solved
            if solve(board):
                return True

        #if board can't be solved it backtracks the last number
        board[row][col] = 0
    return False

solve(board)
print_board(board)
