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


def insert_arrangement(editor):
    # Gerar valores aleatórios para o número de elementos e o número de algarismos
    num_elements = randint(4, 10)
    num_digits = randint(1, num_elements - 1)
    
    # Gerar elementos aleatórios
    elements = list(range(1, num_elements + 1))
    
    # Calcular o número de arranjos
    arrangements_count = factorial(num_elements) // factorial(num_elements - num_digits)
    
    # Gerar todas as combinações possíveis se menor que 150
    all_combinations = []
    if arrangements_count < 150:
        all_combinations = list(permutations(elements, num_digits))
    
    front_text = (
        f"<b>Análise Combinatória - Arranjo Simples</b><br>"
        f"<font color='blue'>Quantas senhas com {num_digits} algarismos diferentes podemos escrever com {num_elements} elementos?</font>"
    )

    
    back_text = (f"<b>Desenvolvimento:</b><br>"
                 f"Formula: Ank = n!/((n-k)!). <br>"
                 f"n → quantidade de elementos que podem ser escolhido. <br>"
                 f"k → quantidade de elementos por agrupamento. <br><br>"
                 f"Utilidade: Podemos aplicar o arranjo simples em várias situações cotidianas, por exemplo, na criação de senhas ou em problemas envolvendo filas.<br>"
                 f"A diferença entre o arranjo e a combinação é que, no arranjo, a ordem dos elementos é relevante, e na combinação, não.<br><br>"

                 f"<b>Exemplo:</b><br>"
		 f"Dado o conjunto de números {1, 2, 3, 4}, podemos listar todos os arranjos simples possíveis que podemos formar com 2 elementos desse conjunto.<br>"
		 f"(1, 2); (1, 3); (1, 4); (2, 1); (2, 3); (2, 4); (3, 1); (3, 2); (3, 4); (4, 1); (4, 2); (4, 3).<br>"
		 f"Então, podemos afirmar que existem 12 arranjos possíveis de 4 elementos tomados de 2 em 2.<br><br>"





#                 f"<font color='blue'>Então, temos {num_elements} elementos para serem agrupados de {num_digits} a {num_digits}. Desta maneira, o cálculo será:</font><br>"
#                 f"A{num_elements},{num_digits} = {num_elements}! / ({num_elements}-{num_digits})!<br>"
#                 f"A{num_elements},{num_digits} = {num_elements}! / {num_elements - num_digits}!<br>"
#                 f"A{num_elements},{num_digits} = {num_elements}!"
#                 f" / {num_elements - num_digits}!<br>"
#                 f"A{num_elements},{num_digits} = {factorial(num_elements) // factorial(num_elements - num_digits)} senhas")
    
#    if arrangements_count < 150:
#        back_text += "<br><br>As combinações possíveis são:<br>"
#        for combination in all_combinations:
#            back_text += f"{''.join(map(str, combination))}<br>"



		 f"<font color='blue'>Então, temos {num_elements} elementos para serem agrupados de {num_digits} a {num_digits}. Desta maneira, o cálculo será:</font><br>"
                 f"A{num_elements},{num_digits} = {num_elements}! / ({num_elements}-{num_digits})!<br>"
    		 f"A{num_elements},{num_digits} = {num_elements}! / {num_elements - num_digits}!<br>"
    		 f"A{num_elements},{num_digits} = {num_elements}! / {num_elements - num_digits}!<br>"
    		 f"A{num_elements},{num_digits} = {factorial(num_elements) // factorial(num_elements - num_digits)} senhas<br>"

		 f"<br>Obs: Este codigo foi feito para mostrar ate 150 combinações possiveis, para nao sobrecarregar o anki ou travar.")

    if arrangements_count < 150:
        back_text += "<br><br>As combinações possíveis são:<br>"
        #for combination in all_combinations:
        for idx, combination in enumerate(all_combinations, start=1):
            #back_text += f"{{{', '.join(map(str, combination))}}}<br>"
            #back_text += f"{idx}-{{{', '.join(map(str, combination))}}}<br>" #fica entre { }
            back_text += f"{idx}-({', '.join(map(str, combination))})<br>"    #fica entre ( )



    
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
    shortcut = QShortcut(QKeySequence("Ctrl+Alt+N"), editor.widget)
    shortcut.activated.connect(lambda: insert_arrangement(editor))

# Registrando a função para quando o editor for criado
gui_hooks.editor_did_init.append(setup_shortcut)

