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






def insert_div_4(editor):

    # Gerar um número aleatório entre 1 e 99999
    number = random.randint(1, 99999)

    # Texto para a frente da carta
    front_text = f"<b>Divisibilidade por 4</b><br><font color='blue'>Diga se o número {number} é divisível por 4 ou não?</font>"

    # Verificação de divisibilidade
    if number % 100 == 0 or number % 4 == 0:
        # Desenvolvimento do verso da carta se for divisível por 4
        explanation_text = (
            f"<b>Desenvolvimento</b><br>"
            f"Pra ser divisível por 4 o final do número tem que ter 00 ou os 2 últimos números "
            f"serem divisíveis por 4. Por exemplo, 20500 e 70832.<br>"
            f"No caso do número {number}, "
        )
        if number % 100 == 0:
            explanation_text += "termina com 00."
        else:
            last_two_digits = number % 100
            if last_two_digits % 4 == 0:
                explanation_text += f"os 2 últimos números ({last_two_digits}) são divisíveis por 4."

        if number % 4 == 0:
            explanation_text += f"<br><br>Sim, o número é divisível por 4, pois {number} / 4 = {number // 4}."
        else:
            explanation_text += "<br><br>Não, o número não é divisível por 4."

    else:
        # Desenvolvimento do verso da carta se não for divisível por 4
        explanation_text = (
            f"<b>Desenvolvimento</b><br>"
            f"Pra ser divisível por 4 o final do número tem que ter 00 ou os 2 últimos números "
            f"serem divisíveis por 4. Por exemplo, 20500 e 70832.<br>"
            f"No caso do número {number}, "
        )
        if number % 100 == 0:
            explanation_text += "termina com 00, mas o número não é divisível por 4, pois não atende aos critérios completos."
        else:
            last_two_digits = number % 100
            if last_two_digits % 4 == 0:
                explanation_text += f"os 2 últimos números ({last_two_digits}) são divisíveis por 4, mas o número não termina com 00."

        explanation_text += "<br><br>Não, o número não é divisível por 4."

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
