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





def insert_produto_potenciacao(editor):
    # Gerar base e expoente aleatórios
    base = random.randint(1, 10)
    expoente = random.randint(0, 10)
    
    # Calcular a potenciação
    resultado = base ** expoente
    

    # Inicializar o texto da frente
    #front_text = ""

    # Montar o texto da frente
    front_text = (
        f"<b>Potenciação</b><br>"
        f"<font color='blue'>Resolva a seguinte potenciação: {base}<sup>{expoente}</sup></font>"
    )
    
    # Montar o texto do verso
    back_text = (
        f"<b>Desenvolvimento:</b><br>{base}"
    )
    
    for i in range(expoente-1):
        back_text += f".{base}"
    back_text += f" = {resultado}<br><br>"
    
    back_text += (
        f"<b>Potenciação ou Exponenciação</b> é a multiplicação de fatores iguais ou um número multiplicado por ele mesmo várias vezes<br>"
        f"a<sup>n</sup> = a.a.a..., sendo 'a' ≠ de 0<br>"
        f"a = base; número que está sendo multiplicado por ele mesmo<br>"
        f"n = expoente; número de vezes que o número é multiplicado<br>"
        f"Exemplo: 2<sup>3</sup> = 2.2.2 = 8 é a potência (resultado do produto)"
    )
    

    



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