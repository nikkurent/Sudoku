from random import randint, shuffle

# Set empty board
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


# Puts random numbers in places with 0, while following the rules of Sudoku
def fill_board(board):
    find = find_zero(board)
    if not find:
        return True
    else:
        row, col = find

    numbers = [1,2,3,4,5,6,7,8,9]
    shuffle(numbers)
    for number in numbers:
        # if is_valid == True --> place number in board
        if is_valid(board, number, (row,col)): 
            board[row][col] = number

            # Retruns True is board is filed
            if fill_board(board):
                return True

            #if board can't be solved it backtracks the last number
            board[row][col] = 0
    return False


# Removes as many random numbers from board while still solvable
def create_sudoku(board):
    for i in range(0, 81):
        row = randint(0,8)
        col = randint(0,8)
        board[row][col] = 0
        for number in range(1, 10):
            # if is_valid == True --> place number in board
            if is_valid(board, number, (row,col)): 
                board[row][col] = 0
    return board


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

# Starts the game based on player input
def start_game():
    player_input = input('Do you want a new game of Sudoku? --> y/n\n')
    if player_input == 'y':
        fill_board(board)
        create_sudoku(board)
        print_board(board)
        _input = input('Do you want it solved --> [y/n]\n')
        if _input == 'y':
            solve(board)
            print_board(board)
    else:
        print('ok, bye')

start_game()