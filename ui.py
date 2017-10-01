from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.inputGrid = [[], [], [], [], [], [], [], [], []]

        grid = QtWidgets.QGridLayout()
        for x in range(0, 9):
            for y in reversed(range(0, 9)):
                grid_space = QtWidgets.QLineEdit()
                # We have to use RegExp because IntValidator doesn't let us do number ranges the way we want to.
                grid_space.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("^[1-9]$")))
                grid_space.setMaxLength(1)
                grid_space.setAlignment(QtCore.Qt.AlignCenter)
                grid_space.setFixedWidth(20)
                grid.addWidget(grid_space, y, x)
                self.inputGrid[x].append(grid_space)

        self.solveButton = QtWidgets.QPushButton()
        self.solveButton.setText("Solve")
        grid.addWidget(self.solveButton, 9, 0, 9, 9)

        self.setLayout(grid)
        self.setFixedSize(250, 250)
        self.setWindowTitle("Sudoku Solver")
        self.show()

    def get_grid_value(self, x, y):
        return self.inputGrid[x][y].text()
