import vocabulary_selector as vc
import checker

import sys
import string
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                            QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton,
                            QSizePolicy, QRadioButton, QButtonGroup, QLineEdit,
                            QSlider)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Německé slovíčka")
        self.setGeometry(500, 300, 750, 400)
        self.phase = 0
        self.points = {"correct": 0, "wrong": 0}
        self.drawUI()
        self.distributor()

    def drawUI(self):
        # creating widgets
        self.mainText = QLabel("Text", self)
        self.results = QLabel("<span style='color: lime;'>Correct: 0</span>"
                              "<br>"
                              "<span style='color: red;'>Wrong: 0</span>", self)
        self.mainInput = QLineEdit(self)
        self.mainButton = QPushButton("Zkontrolovat", self)
        # editing widgets
        self.mainButton.pressed.connect(self.distributor)
        self.results.setAlignment(Qt.AlignmentFlag.AlignCenter)
        for widget in [self.mainText, self.results, self.mainInput, self.mainButton]:
            widget.setStyleSheet("font-size: 30px;")

            widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # layouts and etc...
        self.gridLayout = QGridLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.gridLayout)
        self.setCentralWidget(self.central_widget)
        
        # adding wigets to layout
        self.gridLayout.addWidget(self.mainText, 0, 0)
        self.gridLayout.addWidget(self.results, 0, 1)
        self.gridLayout.addWidget(self.mainInput, 1, 0)
        self.gridLayout.addWidget(self.mainButton, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 3)
        self.gridLayout.setRowStretch(1, 2)

    def distributor(self):
        match self.phase:
            case 0:
                self.phase = 1
                self.input()
            case 1:
                self.phase = 0
                self.output()

    def input(self):
        question_type, cz, cz_visi, de, de_gender, de_gender_visi, de_visi, description = vc.choose_word()
        self.vars = {
            "question_type": question_type,
            "cz": cz,
            "cz_visi": cz_visi,
            "de": de,
            "de_gender": de_gender,
            "de_gender_visi": de_gender_visi,
            "de_visi": de_visi,
            "description": description
        }
        self.mainText.setText(checker.word_getter(question_type, cz_visi, de_visi, description))

    def output(self):
        output = checker.answer_checker(self.mainInput.text(), 
                               self.vars["question_type"], self.vars["cz"], self.vars["cz_visi"], self.vars["de"], 
                                self.vars["de_gender"], self.vars["de_gender_visi"], self.vars["de_visi"])
        self.mainText.setText(f"{output[0]}<br>"
                              f'{f"Tvá odpověď: {self.mainInput.text()}<br>" if output[1] else ""}'
                              f"Němčina: {output[2]}<br>"
                              f"Čeština: {output[3]}")
        if output[4]:
            self.points.update({"correct": self.points["correct"]+1})
        elif not output[4]:
            self.points.update({"wrong": self.points["wrong"]+1})
        self.results.setText(f"<span style='color: lime;'>Correct: {self.points['correct']}</span>"
                              "<br>"
                              f"<span style='color: red;'>Wrong: {self.points['wrong']}</span>")
        



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()