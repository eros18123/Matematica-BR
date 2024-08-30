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



def insert_rule_of_three_simple(editor):
    
    # Gerar valores aleatórios para a regra de três simples
    quantity_1 = random.randint(1, 5)
    unit_1 = random.randint(100, 10000)
    quantity_2 = random.randint(quantity_1 + 1, 10)
    total_unit = (unit_1 * quantity_2) / quantity_1

    # Montar a parte da frente do texto
    front_text = (f"<b>Regra de 3 Simples - Massa ou Peso</b><br>"
                  f"<font color='blue'>Para fazer {quantity_1} bolo(s) de aniversário utilizamos {unit_1} gramas de chocolate. "
                  f"No entanto, faremos {quantity_2} bolos. Qual a quantidade de chocolate que necessitaremos?</font>")

    # Montar a parte de trás do texto com a tabela HTML
    back_text = (f"<b>Desenvolvimento</b><br>"
                 f"Inicialmente, é importante agrupar as grandezas da mesma espécie em duas colunas, a saber:<br><br>"
                 f"<table border='1'>"
                 f"<tr><th>Bolos</th><th>Quantidade (g)</th></tr>"
                 f"<tr><td>{quantity_1}</td><td>{unit_1}g</td></tr>"
                 f"<tr><td>{quantity_2}</td><td>x</td></tr>"
                 f"</table><br>"
                 f"Nesse caso, x é a nossa incógnita, ou seja, o quarto valor a ser descoberto. "
                 f"Feito isso, os valores serão multiplicados de cima para baixo no sentido contrário:<br><br>"
                 f"{quantity_1}x = {unit_1} . {quantity_2}<br>"
                 f"{quantity_1}x = {unit_1 * quantity_2} g<br>"
                 f"x = {unit_1 * quantity_2} / {quantity_1} = {total_unit:.2f} g<br><br>"
                 f"Logo, para fazer os {quantity_2} bolos, precisaremos de {total_unit:.2f} g de chocolate ou {total_unit / 1000:.2f} kg.")

    # Atualizar os campos da nota no editor do Anki
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