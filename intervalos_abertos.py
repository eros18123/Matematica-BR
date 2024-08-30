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


def insert_numeric_interval_aberto(editor):
    """Generate Anki card for numeric interval."""

    # Function to generate random values for A and B ensuring A < B
    def generate_random_ab():
        A = randint(1, 9)  # A varies from 1 to 9
        B = randint(A + 1, 10)  # B varies from A+1 to 10
        return A, B

    # Generate values for A and B
    A, B = generate_random_ab()

    # Build the front text for the Anki card
    front_text = (f"<b>Intervalos Númericos Abertos</b><br>"
                  f"Faça o intervalo aberto de extremos entre A e B<br>"
                  f"Sendo A={A} e B={B}")
                  

    # Build the back text for the Anki card with the specified table structure
    back_text = (f"<b>Desenvolvimento:</b><br>"
                 f"<table style='width:50%;'>"
                 f"  <tr>"
                 f"    <td style='width:5cm;'></td>"
                 f"    <td style='width:1cm; text-align:center;'><div style='width:100%; text-align:center; height: 10px; width: 10px; border-radius: 50%; background-color: white; margin: 0 auto; border: 5px solid black;'></div></td>"

                 f"    <td style='width:5cm;'></td>"
                 #f"    <td style='width:1cm;text-align:center;'>o</td>"
                 f"    <td style='width:1cm; text-align:center;'><div style='width:100%; text-align:center; height: 10px; width: 10px; border-radius: 50%; background-color: white; margin: 0 auto; border: 5px solid black;'></div></td>"
                 f"    <td style='width:5cm;'></td>"
                 f"  </tr>"
                 f"  <tr>"
                 f"    <td style='width:1cm; border-top: 5px solid black;'></td>"
                 f"    <td style='width:1cm; border-top: 5px solid black; text-align:center;'>{A}</td>"
                 f"    <td style='width:1cm; border-top: 5px solid red;'></td>"
                 f"    <td style='width:1cm; border-top: 5px solid black; text-align:center;'>{B}</td>"
                 f"    <td style='width:1cm; border-top: 5px solid black;'></td>"
                 f"  </tr>"
                 f"</table>"
                 f" ]{A}, {B}[ ou ({A}, {B}) = {{XER | {A} < X < {B}}}")




    # Atualizar os campos na nota do editor
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

