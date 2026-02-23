import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                            QGridLayout, QPushButton,
                            QSizePolicy, QRadioButton, QButtonGroup)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password generator")
        self.setGeometry(200, 200, 500, 400)
        
        self.layout = QGridLayout()
        
        self.radio_group = QButtonGroup()
        self.radio1 = QRadioButton("Možnost 1")
        self.radio2 = QRadioButton("Možnost 2")
        self.radio3 = QRadioButton("Možnost 3")
        self.radio_group.addButton(self.radio1, 1)
        self.radio_group.addButton(self.radio2, 2)
        self.radio_group.addButton(self.radio3, 3)
        self.radio1.setChecked(True)

        self.layout.addWidget(self.radio1)
        self.layout.addWidget(self.radio2)
        self.layout.addWidget(self.radio3)

        self.setLayout(self.layout)
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()