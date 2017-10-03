# With regards to the grid, let it be said that if we're referencing it
# using the grid[x][y] syntax, it will be rotated 90 degrees when printed.
# Logically, it will function the same it just may be a little confusing
# when trying to read the sudoku in printed form

# Module Imports
import sys
from PyQt5 import QtWidgets

# Local Imports
import ui

app = QtWidgets.QApplication(sys.argv)  # Create the base QT Application.
window = ui.MainWindow()  # Create the MainWindow class.

grid = []
for i in range(0, 9):
    grid.append([None, None, None, None, None, None, None, None, None])

def solve():
    for x, grid_column in enumerate(grid):  # Go through the columns of the grid.
        for y in range(len(grid_column)):  # Go through the individual numbers in the column.
            grid_value = window.get_grid_value(x, y)  # Get the value on the UI.
            if grid_value == "":  # If it is blank...
                grid_column[y] = None  # ...put nothing...
            else:  # ...or if there is something...  ( We don't need to validate because we do that in the UI. )
                grid_column[y] = int(grid_value)  # ...put the number in.
    print( grid )
    return

window.solveButton.clicked.connect(solve)  # Attach the solve function to the button on the UI.
app.exec_()  # Start the UI.
