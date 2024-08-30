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



from math import sqrt




def insert_real(editor):
    """Generate Anki card for real (R) or complex number (C) check."""

    def is_real_number(n):
        """Check if a number is a real number (R)."""
        return n >= 0

    # Function to generate a real number with a positive square root
    def generate_real_number():
        base = random.randint(1, 100)  # Generating a base for a real number
        return f"√{base} = {sqrt(base):.2f}"

    # Function to generate a complex number with a negative square root
    def generate_complex_number():
        base = random.randint(1, 100)  # Generating a base for a complex number
        return f"√-{base} = {sqrt(base):.2f}i"

    # Decide the type of number to generate
    if random.random() < 0.5:
        number = generate_real_number()
        is_real = True
    else:
        number = generate_complex_number()
        is_real = False

    # Build the front text for the Anki card
    front_text = f"<b>Números Reais ou Complexos</b><br>Diga se o número {number} é um número real (R) ou complexo (C)."

    # Build the back text for the Anki card
    if is_real:
        back_text = (f"<b>Desenvolvimento</b><br>"
                     f"Os números reais (R) incluem todos os números naturais, inteiros, racionais e irracionais.<br>"
                     f"Exemplos: √4 = 2, √9 = 3, √2 ≈ 1.41<br><br>"
                     f"Sim, {number} é um número real (R)<br>")
    else:
        back_text = (f"<b>Desenvolvimento</b><br>"
                     f"Os números complexos (C) incluem números que possuem uma parte imaginária.<br>"
                     f"Exemplos: √-1 = i, √-4 = 2i, √-9 = 3i<br><br>"
                     f"Não, {number} não é um número real (R), é um número complexo (C).<br>")

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
