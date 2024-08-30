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





def insert_div_8(editor):

    # Gerar um número aleatório entre 1 e 99999
    number = random.randint(1, 99999)

    # Texto para a frente da carta
    front_text = f"<b>Divisibilidade por 8</b><br><font color='blue'>Diga se o número {number} é divisível por 8 ou não?</font>"

    # Verificação de divisibilidade por 8
    is_divisible_by_8 = False
    if number >= 100:
        last_three_digits = number % 1000
        if last_three_digits % 8 == 0:
            is_divisible_by_8 = True

    # Desenvolvimento do verso da carta
    explanation_text = (
        f"<b>Desenvolvimento</b><br>"
        f"Em caso de números com 3 dígitos ou mais, para ser divisível por 8, os 3 últimos números precisam ser divisíveis por 8.<br>"
        f"Por exemplo, 11064, os últimos 3 números (064) terminam com número divisível por 8, "
        f"(064) / 8 = 8, ou seja, divisão exata com resto 0.<br>"
        f"Para ser divisível por 8, o final dos últimos 3 números deve ser 000, 008, 016, 024, 032, 040, 048, 056, 064, 072, 080, 088, 096, 104..."
    )

    if is_divisible_by_8:
        explanation_text += f"<br><br>Sim, o número é divisível por 8, pois os últimos 3 números ({number % 1000}) "
        explanation_text += f"terminam com número divisível por 8.<br>"
        explanation_text += f"{number} / 8 = {number // 8}."
    else:
        explanation_text += f"<br><br>Não, o número não é divisível por 8, pois os últimos 3 números ({number % 1000}) "
        explanation_text += f"não terminam com número divisível por 8."

    # Texto para o verso da carta
    back_text = explanation_text

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

