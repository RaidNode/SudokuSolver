from PyQt5 import QtCore, QtGui, QtWidgets

def Start():
    m = MainWindow()
    m.show()
    return m

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("Suduko Solver")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Start()
    app.exec_()