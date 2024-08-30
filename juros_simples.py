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

def calculate_simple_interest(capital, taxa_percentual, tempo):
    # Calcula o juro simples
    juro = capital * taxa_percentual / 100 * tempo
    return juro

def calculate_compound_interest(capital, taxa_percentual, tempo_meses):
    # Converte tempo de meses para anos
    tempo_anos = tempo_meses / 12.0
    # Calcula o montante acumulado
    montante = capital * (1 + taxa_percentual / 100)**tempo_anos
    # Calcula o juro composto
    juro = montante - capital
    return montante, juro

def insert_simple_interest(editor):
    # Gerando números aleatórios para o exemplo de juros simples
    capital = random.randint(100, 10000)
    taxa_percentual = random.randint(1, 99)
    tempo = random.randint(1, 100)
    
    juro = calculate_simple_interest(capital, taxa_percentual, tempo)

    taxa_tempo = ((taxa_percentual / 100)*(tempo))
    

    front_text = (
        f"<b>Juros Simples</b><br>"
        f"<font color='blue'>Exemplo: Um capital de R$ {capital},00 foi investido a uma taxa de {taxa_percentual}% a.a. "
        f"para ser retirado após {tempo} anos. Qual será o juro ao final desse tempo?</font>"
    )



    back_text = (f"<b>Desenvolvimento</b><br>"
                 f"Para calcular o juro, utilizamos a fórmula de juros simples:<br>"
                 f"J = C ∙ i ∙ t<br><br>"
                 f"<b>Dados:</b><br>"
                 f"C = R$ {capital},00<br>"
                 f"i = {taxa_percentual}% a.a.<br>"
                 f"t = {tempo} anos<br><br>"
                 f"J = {capital} . {taxa_percentual / 100:.2f} . {tempo}<br>"
                 f"J = {capital} . {taxa_tempo:.4f}<br>"
                 f"J = R$ {juro:.2f}<br>"
                 f"O juro recebido após {tempo} anos será de R$ {juro:.2f}.")
    
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
