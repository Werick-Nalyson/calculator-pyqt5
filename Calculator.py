import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Calculator(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    qt.exec_()
