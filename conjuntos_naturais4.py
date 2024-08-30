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



def insert_natural_odd(editor):
    number = random.randint(1, 999)  # Gera um número natural ímpar de até 3 dígitos
    
    # Verifica se o número gerado é ímpar
    is_odd = number % 2 != 0
    
    # Frente da carta
    front_text = f"<b>Numeros Naturais Impares</b><br>Diga se o número {number} é um número natural ímpar"
    
    # Verso da carta
    if is_odd:
        back_text = f"<b>Desenvolvimento</b><br>Numero natural impar é representado por Ni ou seja, todo numero positivo impar<br>sim, {number} é um número natural ímpar (N).<br>N = {{{', '.join(str(i) for i in range(1, number + 1, 2))}}}"
    else:
        back_text = f"<b>Desenvolvimento</b><br>Numero natural impar é representado por Ni ou seja, todo numero positivo impar<br>nao, {number} não é um número natural ímpar."
        #back_text = f"<b>Desenvolvimento</b><br>nao, {number} não é um número natural ímpar.<br>N = {{{', '.join(str(i) for i in range(1, number, 2))}}}"
    
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