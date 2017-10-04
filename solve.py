from evaluate import *
from random import randint


preset = []


def solve_sudoku(grid):
    for row in range(len(grid)):

        for item in range(len(grid[row])):

            val = grid[row][item]

            if val is not None:
                preset.append([row, item])


    lastConfirmed = []

