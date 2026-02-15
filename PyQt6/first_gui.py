import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton,
                             QSizePolicy)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moje GUI (:")
        self.setGeometry(550, 300, 800, 600)
        self.setWindowIcon(QIcon(r"icon.jpg"))
        self.initUI()
        self.button_count = 0

    def clicked(self):
        print(f"Clicked {self.button_count} times!")
        self.button_count += 1
        self.button.setText(f"Clicked {self.button_count} times!")

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.label1 = QLabel("#1")
        self.label2 = QLabel("#2")
        self.label3 = QLabel("#3")
        self.label4 = QLabel("#4")
        self.label5 = QLabel("#5")
        self.button = QPushButton("Click me!")
        self.button.setStyleSheet("background-color: orange;"
                                  "font-size: 30px;")
        self.button.clicked.connect(self.clicked)

        grid = QGridLayout()

        for label, color in zip([self.label1, self.label2, self.label3, self.label4, self.label5],
                                ["blue", "green", "yellow", "red", "purple"]):
            label.setStyleSheet(f"background-color: {color};")
            label.setFont(QFont("Arial", 30))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        for w in [self.label1, self.label2, self.label3, self.label4, self.label5, self.button]:
            w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.label2, 0, 1)
        grid.addWidget(self.label3, 0, 2)
        grid.addWidget(self.label4, 1, 0)
        grid.addWidget(self.label5, 1, 1)
        grid.addWidget(self.button, 1, 2)

        grid.setRowStretch(0, 1)
        grid.setRowStretch(1, 1)

        central_widget.setLayout(grid)

        #label = QLabel("Hello", self)
        #label.setFont(QFont("Arial", 40))
        #label.setGeometry(20, 20, 400, 80)
        #label.setStyleSheet("color: blue;"
        #                    "background-color: gray;"
        #                    "font-weight: bold;")
        #label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        #picture = QLabel(self)
        ##pixmap = QPixmap(r"PyQt6\icon.jpg") Teoreticky když to nebudu používat, proč bych to měl ukládat
        #picture.setPixmap(QPixmap(r"icon.jpg"))
        #picture.setGeometry(0, 0, 300, 300)
        #picture.setScaledContents(True)
        #picture.setGeometry((self.width() - picture.width()) // 2,
        #                    (self.height() - picture.height()) // 2,
        #                    picture.width(),
        #                    picture.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()