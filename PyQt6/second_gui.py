import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton,
                             QSizePolicy)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.setGeometry(580, 300, 800, 600)
        self.setWindowIcon(QIcon("icon.jpg"))
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.buttons()

    def buttons(self):
        self.button1 = QPushButton("click me!", self)
        self.button1.setStyleSheet("background-color: blue;"
                                  "font-size: 40px;")

        self.grid = QGridLayout()
        self.grid.addWidget(self.button1, 0, 0)

        self.central_widget.setLayout(self.grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()