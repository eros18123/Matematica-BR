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







def insert_div_6(editor):


    # Gerar um número aleatório entre 1 e 99999
    number = random.randint(1, 99999)

    # Texto para a frente da carta
    front_text = f"<b>Divisibilidade por 6</b><br><font color='blue'>Diga se o número {number} é divisível por 6 ou não?</font>"

    # Verificação de divisibilidade por 6
    is_divisible_by_6 = False
    if number % 2 == 0 and sum(int(digit) for digit in str(number)) % 3 == 0:
        is_divisible_by_6 = True

    # Desenvolvimento do verso da carta
    explanation_text = (
        f"<b>Desenvolvimento</b><br>"
        f"Pra ser divisível por 6, o número precisa ser divisível por 2 e 3 ao mesmo tempo.<br>"
        f"Por exemplo, 43722 é divisível por 2 porque termina com número par (2) "
        f"e é divisível por 3 porque a soma dos algarismos (4+3+7+2+2) = 18 é divisível por 3."
    )

    if is_divisible_by_6:
        explanation_text += f"<br><br>Sim, o número {number} é divisível por 6, pois termina com número par ({number % 10}) "
        explanation_text += f"e a soma dos algarismos ({'+'.join(str(digit) for digit in str(number))} = {sum(int(digit) for digit in str(number))}) é divisível por 3.<br>"
        explanation_text += f"Então, {number} / 6 = {number // 6}."
    else:
        last_digit = number % 10
        sum_digits = sum(int(digit) for digit in str(number))
        explanation_text += f"<br><br>Não, o número {number} não é divisível por 6, pois "
        if last_digit % 2 != 0:
            explanation_text += f"termina com número ímpar ({last_digit}), logo não pode ser divisível por 2. "
        if sum_digits % 3 != 0:
            explanation_text += f"a soma dos algarismos ({'+'.join(str(digit) for digit in str(number))} = {sum_digits}) não é divisível por 3."

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
