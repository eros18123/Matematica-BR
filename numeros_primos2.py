import random
import os
import json
import math
from random import randint, sample
from math import factorial
from aqt.qt import *
from aqt.editor import Editor
#from aqt import gui_hooks
from itertools import permutations  # Importando permutations do módulo itertools

from aqt import mw
from anki.hooks import addHook
from anki.notes import Note

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QFileDialog, QInputDialog
from PyQt6.QtGui import QPixmap, QFont, QIcon
from PyQt6.QtCore import Qt
from aqt import gui_hooks, mw









def insert_prime_check(editor):
    """Generate Anki card for checking if a random number is prime."""
    
    def is_prime(n):
        """Check if a number n is prime."""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def generate_prime_number():
        """Generate a random prime number with up to 5 digits."""
        while True:
            number = random.randint(100, 99999)
            if is_prime(number):
                return number
    
    def generate_non_prime_number():
        """Generate a random non-prime number with up to 5 digits."""
        while True:
            number = random.randint(100, 99999)
            if not is_prime(number):
                return number

    def generate_prime_explanation(number):
        """Generate explanation for primality check."""
        explanation = f"<b>Desenvolvimento</b><br>"
        if is_prime(number):
            explanation += f"Sim, o número {number} é primo.<br><br>"
            divisor = 3
            while divisor * divisor <= number:
                if is_prime(divisor):
                    quotient = number // divisor
                    remainder = number % divisor
                    explanation += f"<div>\n<table>\n"
                    explanation += f"<tr><td>{number} |_{divisor}_ (divisor)</td></tr>\n"
                    explanation += f"<tr><td>-{divisor * quotient:3d}  {quotient:3d} (quociente)</td></tr>\n"
                    explanation += f"<tr><td>{remainder:3d} (resto)</td></tr>\n"
                    explanation += f"</table>\n</div>\n"
                    if quotient <= divisor and remainder != 0:
                        explanation += f"Quociente ({quotient}) <= que divisor ({divisor}) e resto diferente de 0, então acaba aqui<br><br>"
                        break
                    explanation += f"Quociente ({quotient}) > que divisor ({divisor}) e resto diferente de 0, então continua a fazer...<br><br>"
                divisor += 2 if divisor > 2 else 1
            if divisor * divisor > number and number % divisor != 0:
                quotient = number // divisor
                remainder = number % divisor
                explanation += f"<div>\n<table>\n"
                explanation += f"<tr><td>{number} |_{divisor}_ (divisor)</td></tr>\n"
                explanation += f"<tr><td>-{divisor * quotient:3d}  {quotient:3d} (quociente)</td></tr>\n"
                explanation += f"<tr><td>{remainder:3d} (resto)</td></tr>\n"
                explanation += f"</table>\n</div>\n"
                explanation += f"Quociente ({quotient}) <= que divisor ({divisor}) e resto diferente de 0, então acaba aqui<br><br>"
            explanation += f"Sim, o número {number} é primo."
        else:
            explanation += f"Não, o número {number} não é primo.<br><br>"
            divisors = []
            for divisor in range(2, number):
                if number % divisor == 0:
                    divisors.append(divisor)
                    quotient = number // divisor
                    remainder = number % divisor
                    explanation += f"<div>\n<table>\n"
                    explanation += f"<tr><td>{number} |_{divisor}_ (divisor)</td></tr>\n"
                    explanation += f"<tr><td>-{divisor * quotient:3d}  {quotient:3d} (quociente)</td></tr>\n"
                    explanation += f"<tr><td>{remainder:3d} (resto)</td></tr>\n"
                    explanation += f"</table>\n</div>\n"
                    explanation += f"Quociente ({quotient}) > que divisor ({divisor}) e resto igual a 0, então não é primo.<br><br>"

            explanation += f"Os divisores de {number} são {', '.join(map(str, divisors))} e {number}."
        return explanation
    
    # Determinando se o número gerado será primo ou não com uma probabilidade de 90%
    if random.random() < 0.5:
        number = generate_prime_number()
    else:
        number = generate_non_prime_number()
    
    # Montando a expressão para a frente da carta
    front_text = f"<b>Numeros Primos 2</b><br>Diga se o número {number} é primo ou não?"
    
    # Montando o texto para o verso da carta
    back_text = generate_prime_explanation(number)
    
    # Atualizando os campos na nota do editor
    #note = editor.note
    #note["Frente"] = front_text
    #note["Verso"] = back_text
    #editor.loadNote()



    # Atualizar os campos na nota do editor
    note = editor.note
    
    # Obter os nomes dos campos
    field_names = list(note.keys())
    
    # Atualizar o primeiro campo com front_text
    if field_names:
        note[field_names[0]] = front_text
    
    # Atualizar o segundo campo com back_text
    if len(field_names) > 1:
        note[field_names[1]] = back_text
    
    # Iterar sobre os campos e atualizar cada um deles com valores genéricos
    for i, field_name in enumerate(field_names):
        if i not in [0, 1]:
            note[field_name] = f"Valor do campo {field_name}"
    
    editor.loadNote()