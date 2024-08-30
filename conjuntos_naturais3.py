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







def insert_numeros_naturais_pares(editor):
    # Gerar um número natural par aleatório
    number = random.randint(-1000, 1000)
    if number % 2 != 0:
        number += 1  # Garante que o número seja par

    # Montando a expressão para a frente da carta
    front_text = f"<b>Numeros Naturais Pares</b><br>Diga se o número {number} é um número natural par"

    # Verificando se o número é natural par
    if number >= 0 and number % 2 == 0:
        is_natural_par = True
        set_text = "N = {" + ', '.join(str(i) for i in range(0, number + 1, 2)) + "}"
        development_text = f"Numero natural par é representado por Np ou seja, todo numero positivo par<br>Sim, {number} é um número natural par.<br>{set_text}"
    else:
        is_natural_par = False
        development_text = f"Numero natural par é representado por Np ou seja, todo numero positivo par<br>Não, {number} não é um número natural par."

    # Montando o texto para o verso da carta
    back_text = f"<b>Desenvolvimento</b><br>{development_text}"

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
