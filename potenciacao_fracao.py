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





def insert_produto_potenciacao_fracao(editor):

    # Gerar números aleatórios para numerador, denominador e expoente
    numerator = random.randint(1, 9)
    denominator = random.randint(1, 9)
    while numerator == denominator:
        denominator = random.randint(1, 9)
    
    exponent = random.randint(-3, 3)
    while exponent == 0:
        exponent = random.randint(-3, 3)
    
    # Montando a expressão para a frente da carta
    front_text = (f"<b>Potenciação - Fração</b><br>"

                  #f"An,k = <br>\\(\\frac{{{numerator}!}}{{({numerator}-{denominator})!}}\\)<br><br>"


                  f"<font color='blue'>Resolva a seguinte potenciação:<br>\\(\\left(\\frac{{{numerator}}}{{{denominator}}}\\right)^{{{exponent}}}\\)</font>")
    
    # Calculando o desenvolvimento
    if exponent > 0:
        num_exp = numerator ** exponent
        denom_exp = denominator ** exponent
        back_text = (f"<b>Desenvolvimento:</b><br>"
                     f"\\(\\left(\\frac{{{numerator}}}{{{denominator}}}\\right)^{{{exponent}}} = \\frac{{{numerator}^{{{exponent}}}}}{{{denominator}^{{{exponent}}}}} = \\frac{{{num_exp}}}{{{denom_exp}}}\\) ")
    else:
        inverse_numerator = denominator
        inverse_denominator = numerator
        positive_exponent = abs(exponent)
        num_exp = inverse_numerator ** positive_exponent
        denom_exp = inverse_denominator ** positive_exponent
        back_text = (f"<b>Desenvolvimento:</b><br>"
                     f"\\(\\left(\\frac{{{numerator}}}{{{denominator}}}\\right)^{{{exponent}}} = \\left(\\frac{{{inverse_numerator}}}{{{inverse_denominator}}}\\right)^{{{positive_exponent}}} = "
                     f"\\frac{{{inverse_numerator}^{{{positive_exponent}}}}}{{{inverse_denominator}^{{{positive_exponent}}}}} = \\frac{{{num_exp}}}{{{denom_exp}}}\\)")
    


    
  



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
    shortcut = QShortcut(QKeySequence("Ctrl+Alt+V"), editor.widget)
    shortcut.activated.connect(lambda: insert_produto_potenciacao_fracao(editor))

# Registrando a função para quando o editor for criado
gui_hooks.editor_did_init.append(setup_shortcut)
