# Module Imports
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QWidget):  # Create our MainWindow class.
    def __init__(self):  # Function ran when it is created.
        QtWidgets.QWidget.__init__(self)  # Create a base widget.
        self.inputGrid = [[], [], [], [], [], [], [], [], []]  # Create a table to store the LineEdits.

        grid = QtWidgets.QGridLayout()  # Create a GridLayout.
        for x in range(0, 9):
            for y in reversed(range(0, 9)):
                grid_space = QtWidgets.QLineEdit()  # Create a LineEdit
                # We have to use RegExp because IntValidator doesn't let us do number ranges the way we want to
                # and it's not worth the effort of making our own QValidator class.
                grid_space.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("^[1-9]$")))
                grid_space.setMaxLength(1)  # Set max entry length to 1.
                grid_space.setAlignment(QtCore.Qt.AlignCenter)  # Align text to the middle.
                grid_space.setFixedWidth(20)  # Cap the width of the box to 20px.
                grid.addWidget(grid_space, y, x)  # Create it.
                self.inputGrid[x].append(grid_space)  # Add it to our table.

        self.solveButton = QtWidgets.QPushButton()  # Create a button.
        self.solveButton.setText("Solve")  # Set the button text to solve.
        grid.addWidget(self.solveButton, 9, 0, 9, 9)  # Add the button to the grid.

        self.setLayout(grid)  # Set the window layout to use the grid.
        self.setFixedSize(250, 250)  # Set the windows size and prevent resizing.
        self.setWindowTitle("Sudoku Solver")  # Set the title of the window.
        self.show()  # Make the window appear.

    def get_grid_value(self, x, y):  # Function to get the value entered in a specific part of the grid.
        return self.inputGrid[x][y].text()  # Returns the value as a string.
