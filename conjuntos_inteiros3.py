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




def insert_nonnegative_integer_number(editor):
    """Generate Anki card for nonnegative integer number (Z+) check."""
    
    def is_integer_number(n):
        """Check if a number is a nonnegative integer number (Z+)."""
        return isinstance(n, int) and n >= 0
    
    def generate_nonnegative_integer_set(n):
        """Generate the set of nonnegative integers from 0 to n."""
        return set(range(0, n + 1))
    
    # Decide randomly if the number should be an integer or have decimal places (50% chance each)
    if random.choice([True, False]):
        # Generate a random number with up to two decimal places between -999 and 999
        number = round(random.uniform(-999, 999), 2)
    else:
        # Generate a random integer between -999 and 999
        number = random.randint(-999, 999)
    
    # Check if the number is a nonnegative integer
    is_nonnegative_integer = is_integer_number(number)
    
    # Montando a expressão para a frente da carta
    front_text = f"<b>Numeros Inteiros Não Negativos</b><br>Diga se o número {number} é inteiro não negativo (Z+)"
    
    # Montando o texto para o verso da carta
    if is_nonnegative_integer:
        nonnegative_integer_set = generate_nonnegative_integer_set(int(number))
        nonnegative_integer_set_str = ", ".join(map(str, sorted(nonnegative_integer_set)))
        back_text = f"<b>Desenvolvimento</b><br>Sim, {number} é um número inteiro não negativo (Z+)<br>Z+ = {{{nonnegative_integer_set_str}}}"
    else:
        back_text = f"<b>Desenvolvimento</b><br>Não, {number} não é um número inteiro não negativo (Z+)"
    
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

