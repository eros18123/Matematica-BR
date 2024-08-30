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



def insert_repeating_decimal(editor):
    """Generate Anki card for repeating decimal (dízima periódica) check."""

    def is_repeating_decimal(number):
        """Check if a number is a repeating decimal."""
        str_number = str(number).split('.')[1]
        if len(str_number) == 7:  # If exactly 7 digits after decimal, adjust to 6 or 9
            return False
        if len(str_number) < 6 or len(str_number) > 9:
            return False
        for i in range(1, len(str_number) // 2 + 1):
            if str_number[:i] * (len(str_number) // i) == str_number:
                return True
        return False

    def generate_repeating_set(number):
        """Generate the repeating decimal explanation."""
        str_number = str(number).split('.')[1]
        for i in range(1, len(str_number) // 2 + 1):
            if str_number[:i] * (len(str_number) // i) == str_number:
                return str_number[:i]
        return ""

    # Generate a random integer part and a random non-repeating decimal part
    integer_part = random.randint(1, 999)
    
    # Decide randomly if the number will be repeating decimal or not
    if random.choice([True, False]):
        # Generate the number as a repeating decimal
        repeat_length = random.choice([1, 2, 3])  # 1 for single, 2 for double, 3 for triple repeat
        repeating_part = ''.join([str(random.randint(0, 9)) for _ in range(repeat_length)])
        if repeat_length == 3:
            number = float(f"{integer_part}.{repeating_part * (9 // len(repeating_part))}")
        else:
            number = float(f"{integer_part}.{repeating_part * (6 // len(repeating_part))}")
        is_repeating = True
    else:
        # Generate the number as a non-repeating decimal
        decimal_part = ''.join([str(random.randint(0, 9)) for _ in range(random.randint(6, 9))])
        number = float(f"{integer_part}.{decimal_part}")
        is_repeating = False

    # Check if the number is a repeating decimal
    if is_repeating:
        is_repeating = is_repeating_decimal(number)

    # Front text of the card
    front_text = f"<b>Dízima Periódica</b><br>Diga se o número {number} é dízima periódica ou não?"

    # Back text of the card
    if is_repeating:
        repeating_set = generate_repeating_set(number)
        back_text = f"<b>Desenvolvimento</b><br>Sim, o número {number} é dízima periódica, pois os números após o ponto decimal ({repeating_set}) se repetem.<br><br>"
        multiplier = 10 ** len(repeating_set)
        back_text += f"{number} "
        #back_text += f"Multiplica por {multiplier}, pois são {len(repeating_set)} ({repeating_set}) repetindo, veja que os números {repeating_set} se repetem, então é dízima periódica.<br>"
        back_text += f"Multiplica por {multiplier}, pois são {len(repeating_set)} (<span style='color: blue'>{repeating_set}</span>) repetindo, veja que os números <span style='color: blue'>{repeating_set}</span> se repetem, então é dízima periódica.<br>"
        back_text += f"Periodo: <span style='color: blue'>{repeating_set}</span>.<br><br>"
        
        back_text += f"<b>Fração Geratriz:</b> ((numero x (10^quantidade_de_numeros_do_periodo)) - numero_sem_dizima) / ((10^quantidade_de_numeros_do_periodo) -1)<br>"
        back_text += f"Exemplo: se o Periodo for 3, entao a quantidade_de_numeros_do_periodo = 10^1=10, se for 59, entao a quantidade_de_numeros_do_periodo = 10^2=100, se for 194, entao a quantidade_de_numeros_do_periodo = 10^3=1000 e assim por diante<br><br>"

        back_text += f"<b>Resolução:</b><br>"
        multiplied_number = int(number * multiplier)
        back_text += f"{number} x {multiplier} = {multiplied_number}<br>"
        back_text += f"{multiplied_number} - {integer_part} = {multiplied_number - integer_part}<br>"
        back_text += f"O número {repeating_set} tem {len(repeating_set)} números que se repetem, então coloca {multiplier-1}x na fórmula abaixo:<br>"
        back_text += f"({multiplied_number - integer_part}) / {multiplier-1} é o mesmo que {number}"
    else:
        back_text = f"<b>Desenvolvimento</b><br>Não, o número {number} não é dízima periódica, pois os números após o ponto decimal não se repetem."

    # Update note fields in the editor
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
