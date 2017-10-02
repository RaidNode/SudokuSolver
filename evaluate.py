def evaluate_row(sudoku, x):

    # Return True for valid row
    # Return False for invalid row

    number_list = []

    # Generate a list of numbers from the numbers in the sudoku
    for number in sudoku[x]:

        if number in number_list and number is not None:

            return False

        else:

            number_list.append(number)

    return True


def evaluate_column(sudoku, y):

    # Return True for valid column
    # Return False for invalid column

    number_list = []

    for row in sudoku:

        if row[y] in number_list and row[y] is not None:

            return False

        else:

            number_list.append(row[y])

    return True


def evaluate_block(sudoku, x, y):

    from math import ceil

    # Return True for valid block
    # Return False for invalid block

    number_list = []

    # Find block x and block y
    block_x = ceil(x / 3) - 1
    block_y = ceil(y / 3) - 1

    # Find lower limits for x and y
    lower_x = int(block_x * 3)
    lower_y = int(block_y * 3)

    for x in range(lower_x, lower_x + 2):

        for y in range(lower_y, lower_y + 2):

            if sudoku[x][y] in number_list and sudoku[x][y] is not None:

                return False

            else:

                number_list.append(sudoku[x][y])

    return True
