from evaluate import *
from random import randint

solving = True

preset = []

row = 0
item = 0


def solve_sudoku(grid):
    global row
    global item
    global solving

    for x in range(len(grid)):

        for y in range(len(grid[row])):

            val = grid[x][y]

            if val is not None:
                preset.append([x, y])

    while solving:

            print(row, item)

            val = [row, item]

            if val not in preset:

                for i in range(9):
                    grid[row][item] = i+1

                    if evaluate_row(grid, row) is False or evaluate_column(grid, item) is False or evaluate_block(grid, row, item):
                        if i == 8:
                            row, item = back(row, item)
                            print("yeet")
                    else:
                        print( "breakin the law" )
                        next_item()
                        break


def back(x, y):
    y -= 1

    if y < 0:
        y = 9
        x -= 1

    if y < 0 and x < 0:
        print('Invalid sudoku')

    return x, y


def next_item():
    global row
    global item
    global solving

    item += 1

    if item > 8:
        row += 1

    if row > 8:
        solving = False


