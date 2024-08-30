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


def insert_integer_number(editor):

    """Generate Anki card for integer number (Z) check."""
    
    def is_integer_number(n):
        """Check if a number is an integer number (Z)."""
        return isinstance(n, int)
    
    def generate_integer_set(n):
        """Generate the set of integers from -n to n."""
        return set(range(-n, n + 1))
    
    # Decide randomly if the number should be an integer or have decimal places (50% chance each)
    if random.choice([True, False]):
        # Generate a random number with up to two decimal places between -999 and 999
        number = round(random.uniform(-999, 999), 2)
    else:
        # Generate a random integer between -999 and 999
        number = random.randint(-999, 999)
    
    # Check if the number is an integer
    is_integer = is_integer_number(number)




    # Caminho da imagem no addon
    addon_img_path = os.path.join(os.path.dirname(__file__), 'conjuntos_inteiros.png')
    
    # Caminho da imagem na pasta de mídia do Anki
    media_dir = editor.mw.col.media.dir()
    anki_img_path = os.path.join(media_dir, 'conjuntos_inteiros.png')
    
    # Copiar a imagem para a pasta de mídia do Anki
    shutil.copyfile(addon_img_path, anki_img_path)




    
    # Montando a expressão para a frente da carta
    front_text = f"<b>Numeros Inteiros</b><br>Diga se o número {number} é inteiro ou não"
    
    # Montando o texto para o verso da carta
    if is_integer:
        integer_set = generate_integer_set(abs(int(number)))
        integer_set_str = ", ".join(map(str, sorted(integer_set)))
        if number > 0 and number % 2 != 0:
            back_text = (f"<b>Desenvolvimento</b><br>"
                         f"Obs: Numeros inteiros (Z) vão do infinito negativo ate infinito positivo <br>"
                         f"<img src='conjuntos_inteiros.png' style='max-width:100%; height:auto;'><br>"
                         f"Sim, {number} é um número inteiro (Z)<br>Além disso, {number} é um número natural ímpar (N)<br>Z = {{{integer_set_str}}}<br>")



        else:
            back_text = (f"<b>Desenvolvimento</b><br>"
                         f"Obs: Numeros inteiros (Z) vão do infinito negativo ate infinito positivo <br>"
                         f"<img src='conjuntos_inteiros.png' style='max-width:100%; height:auto;'><br>"
                         f"Sim, {number} é um número inteiro (Z)<br>Z = {{{integer_set_str}}}<br>")

    else:
        back_text = (f"<b>Desenvolvimento</b><br>"
                     f"Obs: Numeros inteiros (Z) vão do infinito negativo ate infinito positivo <br>"
                     f"<img src='conjuntos_inteiros.png' style='max-width:100%; height:auto;'><br>"
                     f"Não, {number} não é um número inteiro (Z) pois tem vírgula<br>")

    
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
