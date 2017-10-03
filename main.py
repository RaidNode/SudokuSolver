# With regards to the grid, let it be said that if we're referencing it
# using the grid[x][y] syntax, it will be rotated 90 degrees when printed.
# Logically, it will function the same it just may be a little confusing
# when trying to read the sudoku in printed form

# Module Imports
import sys
from PyQt5 import QtWidgets

# Local Imports
import ui


def solve():
    print(window.get_grid_value(0, 1))


app = QtWidgets.QApplication(sys.argv)
window = ui.MainWindow()

grid = []

for i in range(0, 9):
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

for x in grid:

    print(x)

window.solveButton.clicked.connect(solve)
app.exec_()
