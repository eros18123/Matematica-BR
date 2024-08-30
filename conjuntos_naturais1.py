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


def insert_natural_number(editor):
    """Generate Anki card for natural number (N) check."""
    
    def is_natural_number(n):
        """Check if a number is a natural number (N)."""
        return n >= 0
    
    def generate_natural_set(n):
        """Generate the set of natural numbers up to n."""
        return set(range(n + 1))
    
    # Generate a random number between -999 and 999
    number = random.randint(-999, 999)
    
    # Check if the number is natural
    is_natural = is_natural_number(number)





    # Caminho da imagem no addon
    addon_img_path = os.path.join(os.path.dirname(__file__), 'conjuntos_naturais.png')
    
    # Caminho da imagem na pasta de mídia do Anki
    media_dir = editor.mw.col.media.dir()
    anki_img_path = os.path.join(media_dir, 'conjuntos_naturais.png')
    
    # Copiar a imagem para a pasta de mídia do Anki
    shutil.copyfile(addon_img_path, anki_img_path)





    
    # Montando a expressão para a frente da carta
    front_text = f"<b>Numeros Naturais</b><br>Diga se o número {number} é natural ou não"
    
    # Montando o texto para o verso da carta
    if is_natural:
        natural_set = generate_natural_set(number)
        natural_set_str = ", ".join(map(str, sorted(natural_set)))
        back_text = (f"<b>Desenvolvimento</b><br>"
                     f"Obs: Numeros naturais (N) vão do 0 ate infinito <br>"
                     f"<img src='conjuntos_naturais.png' style='max-width:100%; height:auto;'><br>"
                     f"Sim, {number} é um número natural (N)<br>N = {{{natural_set_str}}}<br>")



    else:
        back_text = (f"<b>Desenvolvimento</b><br>"
                     f"Obs: Numeros naturais (N) vão do 0 ate infinito <br>"
                     f"<img src='conjuntos_naturais.png' style='max-width:100%; height:auto;'><br>"  
                     f"Não, {number} não é um número natural (N)<br>")


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