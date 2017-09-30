def evaluate_row(sudoku, x):

    # Return True for valid row
    # Return False for invalid row

    number_list = []

    # Generate a list of numbers from the numbers in the sudoku
    for number in sudoku[x]:

        number_list.append(number)

    # Check if every number 1 to 9 appears in the string
    for i in range(1, 10):

        if i not in number_list:

            return False

    return True

# This one is probably quicker
def evaluate_row2(sudoki, x):

    # Return True for valid row
    # Return False for invalid row


    number_list = []

    # Generate a list of numbers from the numbers in the sudoku
    for number in sudoku[x]:

        if number in number_list:

            return False

        else:

            number_list.append(number)

    return True

def evaluate_column(sudoku, y):

    # Return True for valid column
    # Return False for invalid column

    # Do stuff
    return sudoku[y]


def evaluate_block(sudoku, x, y):

    # Return True for valid block
    # Return False for invalid block

    # Do stuff
    return sudoku[x,y]
