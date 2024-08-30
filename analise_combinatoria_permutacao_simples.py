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


def insert_permutation_simple(editor):
    # Escolha aleatória de 10 palavras para exemplo de permutação simples
    words = ["JANELA", "COMPUTADOR", "BOLA", "PROFISSAO", "SINONIMO", "FITA", "BARCO", "SOL", "PORTA", "CADEIRA"]
    word = random.choice(words)
    
    n = len(word)
    permutations = factorial(n)
    
    # Montando o texto para a frente da carta
    front_text = (
        f"<b>Análise Combinatória - Permutação Simples</b><br>"
        f"<font color='blue'>Os diferentes modos de organizar as letras de uma palavra são chamados de anagramas. "
        f"Quantos anagramas existem para a palavra {word}?</font>"
    )

    # Montando o texto para o verso da carta
    back_text = (f"<b>Desenvolvimento:</b><br>"
                 f"Assim, como a palavra {word} possui {n} letras, temos que<br>"
                 f"P{n} = {n}! = ")
    
    # Adicionando cada termo do fatorial
    for i in range(n, 0, -1):
        back_text += str(i)
        if i > 1:
            back_text += " . "
        else:
            back_text += f" = {permutations}<br>"
    
    back_text += (f"Portanto, há {permutations} permutações simples para a palavra {word}.")
    
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
