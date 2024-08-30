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


#import shutil


def insert_cubo_diferenca(editor):
    # Gerar coeficientes aleatórios para a expressão
    coef_a = random.randint(1, 10)
    coef_b = random.randint(1, 10)
    

    
    # Montando a expressão para a frente da carta
    front_text = (f"<b>Produtos Notaveis - Cubo da Diferença</b><br><font color='blue'>Desenvolva a seguinte expressão: ({coef_a}x - {coef_b})^3</font>")
    
    # Calculando o desenvolvimento
    term1 = f"({coef_a}x)^3"
    term2 = f"3 . ({coef_a}x)^2 . {coef_b}"
    term3 = f"3 . {coef_a}x . ({coef_b})^2"
    term4 = f"({coef_b})^3"
    
    # Montando o texto para o verso da carta
    back_text = (f"<b>Desenvolvimento:</b><br>"
                 f"cubo do primeiro termo, menos três vezes o primeiro termo elevado ao quadrado vezes o segundo termo, mais três vezes o primeiro termo vezes o segundo termo elevado ao quadrado, menos o segundo termo elevado ao cubo.<br><br>"
                 f"{term1} - {term2} + {term3} - {term4}<br>"
                 f"{coef_a**3}x^3 - {3 * coef_a**2 * coef_b}x^2 + {3 * coef_a * coef_b**2}x - {coef_b**3}")
                 #f"<img src='br.png' width='30' height='20' alt='BR Image'>")

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
