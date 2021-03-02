import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QWidget


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        

        self.setCentralWidget(self.cw)


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    qt.exec_()
