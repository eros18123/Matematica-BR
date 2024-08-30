import os
import random
import datetime
import json
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QRadioButton, QButtonGroup, QPushButton, QApplication, QDialogButtonBox, QHBoxLayout, QMessageBox
from PyQt6.QtCore import QTimer, Qt


class ExemploPermutacaoSimples(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Exemplo de Permutação Simples")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        example_text = self.show_formula_permutacaosimples()
        example_label = QLabel(example_text)
        example_label.setWordWrap(True)
        
        layout.addWidget(example_label)
        
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)
        
        layout.addWidget(button_box)
        
        self.setLayout(layout)

    def show_formula_permutacaosimples(self):
        n = self.generate_random_number()

        numbers = list(range(n, 0, -1))

        example_text = (
            f"<span style='color: red;'>Analise Combinatoria -> Permutação Simples</span><br>"
            f"Quantas permutações existem de {n} elementos?<br><br>"
            f"Pn = n!<br>"
            f"Pn = {n}!<br>"
            f"Pn = {' x '.join(str(i) for i in numbers)}<br>"
            f"Pn = {self.calculate_permutation(n)}"
        )

        return example_text

    def calculate_permutation(self, n):
        result = 1
        for i in range(n, 0, -1):
            result *= i
        return result

    def generate_random_number(self):
        n = random.randint(3, 10)
        return n


