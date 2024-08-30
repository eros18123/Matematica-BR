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



def insert_rational_number(editor):
    """Generate Anki card for rational number (Q) check."""

    def is_repeating_decimal(n):
        """Check if a number is a repeating decimal."""
        str_n = str(n)
        if '.' in str_n:
            decimal_part = str_n.split('.')[1]
            for i in range(1, len(decimal_part) // 2 + 1):
                if decimal_part[:i] * (len(decimal_part) // i) == decimal_part[:len(decimal_part) // i * i]:
                    return True
        return False
    
    def is_rational_number(n):
        """Check if a number is a rational number (Q)."""
        if isinstance(n, int):
            return True
        str_n = str(n)
        if '.' in str_n:
            decimal_part = str_n.split('.')[1]
            if len(decimal_part) <= 3:
                return True
            if is_repeating_decimal(n):
                return True
        return False

    def generate_rational_set(n):
        """Generate the set of rational numbers with n included."""
        if n < 0:
            return f"{{... {n}, 0, 1 ...}}"
        else:
            return f"{{... -1, 0, {n} ...}}"

    # Function to generate a repeating decimal number
    def generate_repeating_decimal():
        integer_part = random.randint(-999, 999)
        repeating_part = str(random.randint(10, 99))  # Double digit repeating part
        return float(f"{integer_part}.{repeating_part * 5}")  # Repeat the part 5 times

    # Function to generate a non-repeating decimal number
    def generate_non_repeating_decimal():
        integer_part = random.randint(-999, 999)
        non_repeating_part = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        return float(f"{integer_part}.{non_repeating_part}")

    # Function to generate a number with up to 3 decimal places
    def generate_short_decimal():
        integer_part = random.randint(-999, 999)
        decimal_part = ''.join([str(random.randint(0, 9)) for _ in range(random.randint(1, 3))])
        return float(f"{integer_part}.{decimal_part}")

    # Decide the type of number to generate
    if random.random() < 0.5:
        # Generate a non-repeating decimal (irrational)
        number = generate_non_repeating_decimal()
    else:
        # Generate a repeating decimal or a short decimal (rational)
        if random.random() < 0.5:
            number = generate_repeating_decimal()
        else:
            number = generate_short_decimal()

    # Build the front text for the Anki card
    front_text = f"<b>Numeros Racionais</b><br>Diga se o número {number} é racional (Q)"

    # Build the back text for the Anki card
    if is_rational_number(number):
        rational_set = generate_rational_set(number)
        back_text = (f"<b>Desenvolvimento</b><br>"
                     f"Os números racionais são os números que podem ser escritos na forma de fração. Esses números podem também ter representação decimal finita ou decimal infinita e periódica.<br>"
                     f"Q = {{a/b | aEZ, bEZ*}} <br>"
                     f"Q = {{ \"a\" sobre \"b\", tal que, \"a\" pertence aos numeros inteiros e \"b\" pertence aos numeros inteiros nao nulos (menos o zero) }} <br><br>"
                     f"Sim, {number} é um número racional (Q)<br>Q = {rational_set}")
    else:
        back_text = (f"<b>Desenvolvimento</b><br>"
                     f"Os números racionais são os números que podem ser escritos na forma de fração. Esses números podem também ter representação decimal finita ou decimal infinita e periódica.<br>"
                     f"Q = {{a/b | aEZ, bEZ*}} <br>"                     
                     f"Q = {{ \"a\" sobre \"b\", tal que, \"a\" pertence aos numeros inteiros e \"b\" pertence aos numeros inteiros nao nulos (menos o zero) }} <br><br>"            
                     f"Não, {number} não é um número racional (Q)<br>Q = {{...}}")





    # Update the fields in the editor's note
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
