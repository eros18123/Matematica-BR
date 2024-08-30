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


def insert_rule_of_three_simple_time(editor):

    
    # Gerar valores aleatórios para a regra de três simples (tempo e velocidade)
    hours_1 = random.randint(1, 10)
    speed_1 = random.randint(50, 200)
    speed_2 = random.randint(speed_1 + 1, 200)
    distance = speed_1 * hours_1
    hours_2 = distance / speed_2

    # Montar a parte da frente do texto
    front_text = (f"<b>Regra de 3 Simples - Distância ou Tempo</b><br>"
                  f"<font color='blue'>Para chegar em São Paulo, Lisa demora {hours_1} horas numa velocidade de {speed_1} km/h. "
                  f"Assim, quanto tempo seria necessário para realizar o mesmo percurso numa velocidade de {speed_2} km/h?</font>")

    # Montar a parte de trás do texto com a tabela HTML
    back_text = (f"<b>Desenvolvimento</b><br>"
                 f"Da mesma maneira, agrupam-se os dados correspondentes em duas colunas:<br><br>"
                 f"<table border='1'>"
                 f"<tr><th>Velocidade (km/h)</th><th>Tempo (h)</th></tr>"
                 f"<tr><td>{speed_1}</td><td>{hours_1}h</td></tr>"
                 f"<tr><td>{speed_2}</td><td>x</td></tr>"
                 f"</table><br>"
                 f"Observe que ao aumentar a velocidade, o tempo do percurso diminuirá e, tratando-se de grandezas inversamente proporcionais.<br>"
                 f"Em outras palavras, o aumento de uma grandeza implicará na diminuição da outra. Diante disso, invertemos os termos da coluna para realizar a equação:<br><br>"
                 f"{speed_2} km/h - {hours_1}h<br>"
                 f"{speed_1} km/h - x<br><br>"

                 f"{speed_2}x = {speed_1} * {hours_1}<br>"
                 f"{speed_2}x = {speed_1 * hours_1}<br>"
                 f"x = {speed_1 * hours_1} / {speed_2}<br>"
                 f"x = {hours_2:.2f} horas<br><br>"
                 f"Logo, para fazer o mesmo trajeto aumentando a velocidade, o tempo estimado será de {hours_2:.2f} horas.")

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