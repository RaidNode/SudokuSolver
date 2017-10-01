from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.inputGrid = [[], [], [], [], [], [], [], [], []]

        grid = QtWidgets.QGridLayout()
        for x in range(0, 9):
            for y in range(0, 9):
                grid_space = QtWidgets.QLineEdit()
                grid_space.setValidator(QtGui.QIntValidator())
                grid_space.setMaxLength(1)
                grid_space.setAlignment(QtCore.Qt.AlignCenter)
                grid_space.setFixedWidth(20)
                grid.addWidget(grid_space, y, x)
                self.inputGrid[x].append(grid_space)

        self.solveButton = QtWidgets.QPushButton()
        self.solveButton.setText( "Solve" )
        grid.addWidget( self.solveButton, 9, 0, 9, 9 )

        self.setLayout(grid)
        self.setFixedSize( 250, 250 )
        self.setWindowTitle("Sudoku Solver")
        self.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
