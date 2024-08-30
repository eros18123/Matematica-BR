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


def insert_sistemas_numeracao2(editor):
    # Gerar um número aleatório com até 7 dígitos
    numero = random.randint(0, 9999999)
    
    # Formatar número sem pontos
    numero_formatado = f"{numero:07d}"
    
    # Escolher um índice aleatório dentro do número formatado
    indice_digito = random.randint(0, len(numero_formatado) - 1)
    
    # Dígito dentro do número formatado
    digito = numero_formatado[indice_digito]
    
    # Determinar a classe do algarismo destacado em vermelho
    if indice_digito >= len(numero_formatado) - 3:
        classe = "das unidades simples"
    elif indice_digito >= len(numero_formatado) - 6:
        classe = "dos milhares"
    else:
        classe = "dos milhões"
    
    # Montar a expressão para a frente da carta
    front_text = (f"<b>Sistema de Numeração - Classe</b><br><font color='blue'>No número {numero_formatado[:indice_digito]}"
                  f"<font color='red'>{digito}</font>"
                  f"{numero_formatado[indice_digito + 1:]}, qual a classe do algarismo "
                  f"{digito} como sistema de numeração?</font>")
    
    # Montar o texto para o verso da carta
    back_text = (f"<b>Desenvolvimento</b><br>"
                 f"O <font color='red'>{digito}</font> faz parte {classe}.<br><br>"
                 f"<b>Classes:</b><br>"
                 f"{numero_formatado[:-6]}: milhões<br>"
                 f"{numero_formatado[-6:-3]}: milhares<br>"
                 f"{numero_formatado[-3:]}: unidades simples")
    
    # Atualizar os campos na nota do editor
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