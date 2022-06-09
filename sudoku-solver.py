sudoku = [
    [0,1,0,0,8,9,2,0,0],
    [6,8,0,0,0,5,0,3,0],
    [0,9,0,0,0,0,0,7,0],
    [0,0,6,8,5,2,0,4,0],
    [0,0,5,4,0,0,7,0,0],
    [0,0,0,9,7,0,0,0,0],
    [0,0,0,0,0,7,0,0,0],
    [0,0,3,0,0,8,0,2,7],
    [0,5,0,0,0,4,0,0,1]
]

def print_sudoku(board):
    #takes in sudoku board and displays it in the console
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------")

        for j in range(len(board[0])):
            if j %  3 == 0 and j != 0:
                print("|", end = "")

            if j % 8 == 0 and j != 0:
                 print(board[i][j])
            else:
                print(board[i][j], end = "")

def blank_space(board):
    #takes in a board and finds the first blank starting from the top left and checking each row
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None

def validate(board, num, coord):
    #takes board, number, and coordinate to see if the number can go in the given coordinate
    #checks the column for a repeat of the given number
    for i in range(len(board[0])):
        if num == board[coord[0]][i] and coord[1] != i:
            return False

    #checks the row for a repeat of the given number
    for i in range(len(board)):
        if num == board[i][coord[1]] and coord[0] != i:
            return False

    box_x = (coord[1] // 3) * 3
    box_y = (coord[0] // 3) * 3

    #this checks 3x3 grid so see if the given number is already present in the box
    for i in range(3):
            for j in range(3):
                    if num == board[box_y + i][box_x + j] and (i,j != coord):
                        return False
    return True

def solve(board):
    #takes in a board and runs a back treacking algorithm to solve the sudoku, where it precedes if the
    #number tried work. But if eventually no numbers works, it goes back and tries a different number at the last
    #blank spot#
    blank = blank_space(board)
    if not blank:
        return True

    else:
        y, x = blank
        for i in range(1,10):
            if validate(board, i, (y, x)):
                board[y][x] = i

                if solve(board):
                    return True

                board[y][x] = 0

        return False

print_sudoku(sudoku)
solve(sudoku)
print("")
print_sudoku(sudoku)
