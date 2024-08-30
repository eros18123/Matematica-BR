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





def insert_div_9(editor):
    
    def divisibility_by_9_check(num):
        """Verifica a divisibilidade por 9 baseada na soma dos algarismos."""
        steps = ""
        original_num = num
        digit_sum = sum(int(digit) for digit in str(num))

        steps += f"Divisibilidade por 9: a soma dos algarismos é divisível por 9<br>"
        steps += f"numero: {num}<br>"
        steps += f"soma: {'+'.join(str(digit) for digit in str(num))} = {digit_sum}<br>"

        remainder = digit_sum % 9
        quotient = digit_sum // 9

        steps += f"{digit_sum} |_9_ (divisor)<br>"
        steps += f"-{9 * quotient}    {quotient} (quociente)<br>"
        steps += f"{remainder} (resto)<br><br>"

        return remainder == 0, steps, digit_sum

    def check_and_explain(num):
        """Verifica se um número é divisível por 9 e gera a explicação correspondente."""
        explanation_text = ""

        is_divisible, steps, digit_sum = divisibility_by_9_check(num)
        explanation_text += steps

        if is_divisible:
            explanation_text += f"Sim, o número {num} é divisível por 9, pois o resto é igual a zero (0).<br>"
            #explanation_text += f"{digit_sum} / 9 = {digit_sum // 9}"
            explanation_text += f"{num} / 9 = {num // 9}"
        else:
            explanation_text += f"Não, o número {num} não é divisível por 9, pois {digit_sum} dividido por 9 tem o resto igual a {digit_sum % 9}."
        
        return explanation_text

    # Gerar um número aleatório para verificar a divisibilidade por 9
    number_to_check = random.randint(9, 99999)
    front_text = f"<b>Divisibilidade por 9</b><br>Diga se o número {number_to_check} é divisível por 9 ou não?"

    explanation_text = check_and_explain(number_to_check)

    back_text = f"<b>Desenvolvimento</b><br>"
    back_text += explanation_text

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
