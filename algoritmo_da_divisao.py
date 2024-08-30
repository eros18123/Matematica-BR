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


import shutil
from aqt.qt import QAction, QKeySequence






def insert_divisao_algoritmo(editor):

    """Generate Anki card for division algorithm."""
    
    # Generate random values for divisor, quotient, and remainder
    divisor = random.randint(1, 99)
    quotient = random.randint(1, 99)
    remainder = random.randint(0, divisor - 1)
    
    # Calculate the dividend
    dividend = quotient * divisor + remainder
    

    # Caminho da imagem no addon
    addon_img_path = os.path.join(os.path.dirname(__file__), 'algoritmo_da_divisao.jpg')
    
    # Caminho da imagem na pasta de mídia do Anki
    media_dir = editor.mw.col.media.dir()
    anki_img_path = os.path.join(media_dir, 'algoritmo_da_divisao.jpg')
    
    # Copiar a imagem para a pasta de mídia do Anki
    shutil.copyfile(addon_img_path, anki_img_path)


    # Montando a expressão para a frente da carta
    #front_text = f"Ache o dividendo quando o divisor é {divisor}, o quociente é {quotient} e o resto é {remainder}."
   
    front_text = (
        f"<b>Algoritmo da Divisão</b><br>"
        f"Ache o dividendo quando o divisor é {divisor}, o quociente é {quotient} e o resto é {remainder}."
    )

    
    # Montando o texto para o verso da carta
    back_text = (
        f"<b>Desenvolvimento</b><br>"
        f"D = q.d + r<br>"
        f"Obs: o resto é sempre menor que o divisor para que o calculo de certo<br>"
        f"{quotient} . {divisor} + {remainder} = {dividend}<br><br>"

        f"<img src='algoritmo_da_divisao.jpg' style='max-width:100%; height:auto;'> <br><br>"


        f"<b>Cálculo:</b><br>"
        #f"<pre>"
        f"{dividend} |_ {divisor}_ (divisor)<br>"
        f"-{divisor * quotient}  {quotient} (quociente)<br>"
        f"{remainder} (resto)<br>"
        #f"</pre>"
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










# Função para criar o atalho
def setup_shortcut(editor):
    shortcut = QShortcut(QKeySequence("Ctrl+Alt+T"), editor.widget)
    shortcut.activated.connect(lambda: insert_divisao_algoritmo(editor))

# Registrando a função para quando o editor for criado
gui_hooks.editor_did_init.append(setup_shortcut)


