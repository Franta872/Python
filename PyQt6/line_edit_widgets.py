import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton,
                             QSizePolicy, QLineEdit)
from PyQt6.QtGui import QIcon, QPixmap #, QFont
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 500, 900, 300)
        self.setWindowTitle("textbox and button")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.initUI()
    
    def initUI(self):
        self.grid = QGridLayout()

        self.text = QLabel("Text")
        self.text.setStyleSheet("font-size: 50px;"
                                "font-family: Arial;")
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Type something!")
        self.button = QPushButton("Button", self)

        for w in [self.text, self.textbox, self.button]:
            w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.grid.addWidget(self.text, 0, 0)
        self.grid.addWidget(self.textbox, 1, 0)
        self.grid.addWidget(self.button, 1, 1)

        self.central_widget.setLayout(self.grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()