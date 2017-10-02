# Module Imports
import sys
from PyQt5 import QtWidgets

# Local Imports
import ui

app = QtWidgets.QApplication(sys.argv)  # Create the base QT Application.
window = ui.MainWindow()  # Create the MainWindow class.

grid = []

for i in range(0, 9):
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])


def solve():
    grid_value = int(window.get_grid_value(0, 1))  # Gets the value of a grid space from the UI.
    print(grid_value)


window.solveButton.clicked.connect(solve)  # Attach the solve function to the button on the UI.
app.exec_()  # Start the UI.
