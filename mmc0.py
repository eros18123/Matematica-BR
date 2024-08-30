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







def insert_mmc0(editor):
    """Generate Anki card for MMC factorization."""
    
    def factorize(n):
        """Return the factorization of a number n as a dictionary."""
        factors = {}
        divisor = 2
        while n > 1:
           while n % divisor == 0:
                if divisor in factors:
                    factors[divisor] += 1
                else:
                    factors[divisor] = 1
                n //= divisor
           divisor += 1
        return factors
    
    def format_factors(factors):
        """Format the factor dictionary into a readable string."""
        factor_str = ""
        for prime, exponent in factors.items():
            if exponent == 1:
                factor_str += f"{prime}."
            else:
                factor_str += f"{prime}^{exponent}."
        return factor_str.rstrip('.')
    
    # Generate a random number with up to 5 digits
    number = random.randint(2, 99999)
    
    # Factorize the number
    factors = factorize(number)
    
    # Montando a expressão para a frente da carta
    front_text = f"Ache o MMC do número {number}"
    
    # Montando o texto para o verso da carta
    back_text = f"<b>Desenvolvimento</b><br><br>"
    n = number
    factorization_steps = "<table border='1'>"
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factorization_steps += f"<tr><td>{n}</td><td> {divisor}</td></tr>"
            n //= divisor
        else:
            divisor += 1
    factorization_steps += "<tr><td>1</td></tr></table>"
    factorization_str = format_factors(factors)
    back_text += f"{factorization_steps}<br>{number} = {factorization_str}"
    
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

