import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                             QGridLayout, QPushButton,
                             QSizePolicy, QLineEdit, QMessageBox,
                             QDialog, QVBoxLayout, QCheckBox, QDialogButtonBox)
from PyQt6.QtGui import QIcon, QColor #, QPixmap , QFont
from PyQt6.QtCore import Qt

class OptionsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nastavení")
        self.resize(500, 600)

        layout = QVBoxLayout(self)

        self.cb_a = QCheckBox("Chechbox A")
        self.cb_b = QCheckBox("Chechbox B")
        self.cb_c = QCheckBox("Chechbox C")

        layout.addWidget(self.cb_a)
        layout.addWidget(self.cb_b)
        layout.addWidget(self.cb_c)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def values(self):
        return {
            "A": self.cb_a.isChecked(),
            "B": self.cb_b.isChecked(),
            "C": self.cb_c.isChecked(),
        }



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

        self.text = QLabel("Text", self)
        self.text.setStyleSheet("font-size: 50px;"
                                "font-family: Arial;")
        self.text.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.long_text = QLabel(f"<span style='color: lime;'>Correct: 8</span><br>"
                                f"<span style='color: red;'>Wrong: 11</span>",
                                self)
        self.long_text.setStyleSheet("font-size: 30px;")
        self.long_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Type something!")
        self.textbox.setStyleSheet("font-size: 40px")

        self.button = QPushButton("Button", self)
        self.button.setStyleSheet("font-size: 45px;"
                                  "border-radius: 30px;"
                                  "margin: 8px;"
                                  "color: black;"
                                  "background-color: #7209B7;")


        for w in [self.text, self.textbox, self.button]:
            w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.grid.addWidget(self.text, 0, 0)
        self.grid.addWidget(self.long_text, 0, 1)
        self.grid.addWidget(self.textbox, 1, 0)
        self.grid.addWidget(self.button, 1, 1)
        self.grid.setColumnStretch(0, 2)
        self.grid.setColumnStretch(1, 1)
        self.grid.setRowStretch(0, 5)
        self.grid.setRowStretch(1, 4)
        self.central_widget.setLayout(self.grid)

        dlg = OptionsDialog(self)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            print(dlg.values())
        else:
            print("Zrušeno")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()