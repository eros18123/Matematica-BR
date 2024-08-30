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




def insert_no_null_natural_number(editor):
    """Generate Anki card for non-null natural numbers."""
    
    # Generate a random number with up to 3 digits, ranging from -999 to 999
    number = random.randint(-999, 999)
    
    # Determine if the number is a non-null natural number
    if number > 0:
        is_non_null_natural = True
        set_n_star = ', '.join(map(str, range(1, number + 1)))
        back_text = (f"<b>Desenvolvimento</b><br>Numero natural nao nulo é representado por N* ou  N = -{{0}}, ou seja, todo numero positivo, menos o 0<br>sim, {number} é um número natural não nulo (N*).<br>"
                     f"N* = {{{set_n_star}}}")
    else:
        is_non_null_natural = False
        back_text = f"<b>Desenvolvimento</b><br>Numero natural nao nulo é representado por N* ou  N = -{{0}}, ou seja, todo numero positivo, menos o 0<br>não, {number} não é um número natural não nulo (N*)."

    # Montando a expressão para a frente da carta
    front_text = f"<b>Numeros Naturais Não Nulos</b><br>Diga se o número {number} é natural não nulo ou não."

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