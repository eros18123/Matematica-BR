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



def insert_irrational_number(editor):
    """Generate Anki card for irrational number (I) check."""

    def is_repeating_decimal(n):
        """Check if a number is a repeating decimal."""
        str_n = str(n)
        if '.' in str_n:
            decimal_part = str_n.split('.')[1]
            for i in range(1, len(decimal_part) // 2 + 1):
                if decimal_part[:i] * (len(decimal_part) // i) == decimal_part[:len(decimal_part) // i * i]:
                    return True
        return False

    def is_irrational_number(n):
        """Check if a number is an irrational number (I)."""
        if isinstance(n, int):
            return False
        str_n = str(n)
        if '.' in str_n:
            decimal_part = str_n.split('.')[1]
            if len(decimal_part) > 3 and not is_repeating_decimal(n):
                return True
        return False

    # Function to generate a repeating decimal number
    def generate_repeating_decimal():
        integer_part = random.randint(1, 999)  # To avoid zero
        repeating_part = str(random.randint(10, 99))  # Double digit repeating part
        return float(f"{integer_part}.{repeating_part * 5}")  # Repeat the part 5 times

    # Function to generate a non-repeating, non-terminating decimal number
    def generate_irrational_number():
        integer_part = random.randint(1, 999)  # To avoid zero
        irrational_part = ''.join([str(random.randint(0, 9)) for _ in range(random.randint(5, 10))])
        return float(f"{integer_part}.{irrational_part}")

    # Decide the type of number to generate
    if random.random() < 0.5:
        number = generate_repeating_decimal()
        is_irrational = False
    else:
        number = generate_irrational_number()
        is_irrational = True

    # Build the front text for the Anki card
    front_text = f"<b>Números Irracionais</b><br>Diga se o número {number} é irracional (I) ou uma dízima periódica."

    # Build the back text for the Anki card
    if is_irrational:
        back_text = (f"<b>Desenvolvimento</b><br>"
                     f"Os números irracionais são números decimais não exatos, com representação finita e não periódica.<br>"
                     f"Exemplos: 3,141592..., 1,203040..., 1,414213...<br><br>"
                     f"Sim, {number} é um número irracional (I)<br>")
    else:
        back_text = (f"<b>Desenvolvimento</b><br>"
                     f"Os números irracionais são números decimais não exatos, com representação finita e não periódica.<br>"
                     f"Exemplos: 3,141592..., 1,203040..., 1,414213...<br><br>"
                     f"Os números com dízimas periódicas são números decimais que possuem uma parte decimal que se repete infinitamente.<br>"
                     f"Exemplos: 1,202020..., 46,932932..., 459,121212...<br><br>"
                     f"Não, {number} não é um número irracional (I), é uma dízima periódica (Número Racional).<br>")

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
