import sys
import string
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                            QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton,
                            QSizePolicy, QRadioButton, QButtonGroup, QLineEdit,
                            QSlider)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

def PIN(lenght: int):
    return "".join(random.choices(string.digits, k = lenght))
def char(lenght: int):
    return "".join(random.choices(string.ascii_letters, k = lenght))
def pro_passw(lenght: int):
    return "".join(random.choices(string.printable.strip(), k = lenght))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password generator")
        self.setGeometry(200, 200, 800, 500)

        # central widget and layout (grid)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QGridLayout()
        self.central_widget.setLayout(layout)

        # radio buttons
        self.radio_group = QButtonGroup()
        self.PIN_option = QRadioButton("PIN")
        self.characters_option = QRadioButton("Znaky")
        self.proper_password_option = QRadioButton("Pořádné heslo")
        self.radio_group.addButton(self.PIN_option, 1)
        self.radio_group.addButton(self.characters_option, 2)
        self.radio_group.addButton(self.proper_password_option, 3)
        self.PIN_option.setChecked(True)

        self.password_line = QLineEdit()
        self.password_line.setReadOnly(True)
        self.password_line.setStyleSheet("font-size: 20px;")

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(5)
        self.slider.setMaximum(50)
        self.slider.setValue(15)
        self.slider.valueChanged.connect(lambda: self.sliderLabel.setText(f"Délka: {self.slider.value()}"))
        self.sliderLabel = QLabel(f"Délka: {self.slider.value()}")
        self.sliderLabel.setStyleSheet("font-size: 25px;")

        self.button = QPushButton("Vygenerovat heslo")
        self.button.setStyleSheet("font-size: 18px;"
                                  "background-color: purple;"
                                  "border-radius: 50px;" # nefunguje ?!
                                  "padding: 20px;")
        def password_type():
            match self.radio_group.checkedId():
                case 1:
                   return PIN(self.slider.value())
                case 2:
                   return char(self.slider.value())
                case 3:
                   return pro_passw(self.slider.value())
        self.button.clicked.connect(lambda: self.password_line.setText(password_type()))

        # adding widgets to layout
        layout.addWidget(self.PIN_option, 0, 0)
        layout.addWidget(self.characters_option, 0, 1)
        layout.addWidget(self.proper_password_option, 0, 2)
        layout.addWidget(self.button, 2, 2)
        layout.addWidget(self.password_line, 2, 0)
        layout.addWidget(self.sliderLabel, 1, 0)
        layout.addWidget(self.slider, 1, 1)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()