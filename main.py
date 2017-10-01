# Module Imports
import sys
from PyQt5 import QtWidgets

# Local Imports
import ui

app = QtWidgets.QApplication(sys.argv)
window = ui.MainWindow()

grid = []

for i in range(0, 9):
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])


def solve():
    print(window.get_grid_value(0, 1))


window.solveButton.clicked.connect(solve)
app.exec_()
