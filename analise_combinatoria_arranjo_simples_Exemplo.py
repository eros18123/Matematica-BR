import os
import random
import datetime
import json
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QRadioButton, QButtonGroup, QPushButton, QApplication, QDialogButtonBox, QHBoxLayout, QMessageBox
from PyQt6.QtCore import QTimer, Qt


class ExemploArranjoSimples(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Exemplo de Arranjo Simples")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        example_text = self.show_formula_arranjosimples()
        example_label = QLabel(example_text)
        example_label.setWordWrap(True)
        
        layout.addWidget(example_label)
        
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)
        
        layout.addWidget(button_box)
        
        self.setLayout(layout)

    def show_formula_arranjosimples(self):
        n = random.randint(3, 10)
        p = random.randint(1, n-1)

        example_text = (
            f"<span style='color: red;'>Analise Combinatoria -> Arranjo Simples</span><br>"
            f"Quantos arranjos existem de {n} elementos tomados de {p} em {p}?<br><br>"
            f"An,k = n!<br>"
            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_____<br>"
            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(n-k)!<br><br>"
            f"An,k = {n}!<br>"
            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_____<br>"
            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;({n}-{p})!<br><br>"
            f"An,k = {n}!<br>"
            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_____<br>"
            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{n-p}!<br><br>"
            f"An,k = {n} x {' x '.join(str(i) for i in range(n-1, n-p, -1))} = {self.calculate_arrangement(n, p)}"
        )

        return example_text

    def calculate_arrangement(self, n, p):
        result = 1
        for i in range(n, n-p, -1):
            result *= i
        return result


