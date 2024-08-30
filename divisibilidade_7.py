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





def insert_div_7(editor):

    def divisibility_by_7_check(num):
        """Verifica a divisibilidade por 7 e retorna os passos explicativos até o número 7."""
        steps = ""
        original_num = num
        
        while num >= 7:
            unit_digit = num % 10
            rest_number = num // 10
            subtracted_number = rest_number - 2 * unit_digit
            
            if subtracted_number < 7:
                break

            steps += f"<b>Divisibilidade por 7:</b><br>"
            steps += f"separe o algarismo da unidade: {rest_number} e {unit_digit}<br>"
            steps += f"multiplique esse algarismo por 2: {unit_digit} x 2 = {2 * unit_digit}<br>"
            steps += f"subtraia o valor encontrado do restante do número: {rest_number} - {2 * unit_digit} = {subtracted_number}<br><br>"
            
            num = subtracted_number
        
        remainder = num % 7
        quotient = num // 7

        # Corrigir se o resto for negativo
        if remainder < 0:
            remainder += 7
            quotient -= 1

        steps += f"{num} |_7_ (divisor)<br>"
        steps += f"-{7 * quotient}     {quotient} (quociente)<br>"
        steps += f"{remainder} (resto)<br>"

        return steps, remainder, quotient

    def check_and_explain(num):
        """Verifica se um número é divisível por 7 e gera a explicação correspondente."""
        explanation_text = ""

        steps_7, final_num_7, quotient = divisibility_by_7_check(num)
        explanation_text += steps_7

        if final_num_7 == 0:
            explanation_text += f"<br>Sim, o número {num} é divisível por 7, pois o resto ({final_num_7}) é igual a zero (0).<br>"
            explanation_text += f"{num} / 7 = {num // 7}"
        else:
            explanation_text += f"<br>Não, o número {num} não é divisível por 7, pois o resto ({final_num_7}) é diferente de zero."
        
        return explanation_text

    def generate_number():
        """Gera um número aleatório maior ou igual a 7 para o teste de divisibilidade por 7."""
        return random.randint(7, 99999)

    number_to_check = generate_number()

    front_text = f"<b>Divisibilidade por 7</b><br>Diga se o número {number_to_check} é divisível por 7 ou não?"

    explanation_text = check_and_explain(number_to_check)

    back_text = f"<b>Desenvolvimento:</b><br>"
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
