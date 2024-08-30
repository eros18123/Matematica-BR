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





def insert_mmc1(editor):

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
    
    def lcm(a, b):
        """Calculate the Least Common Multiple (LCM) of two numbers."""
        return abs(a*b) // math.gcd(a, b)
    
    def format_factors(factors):
        """Format the factor dictionary into a readable string."""
        factor_str = ""
        for prime, exponent in factors.items():
            if exponent == 1:
                factor_str += f"{prime}."
            else:
                factor_str += f"{prime}^{exponent}."
        return factor_str.rstrip('.')
    
    def combined_factors(factors1, factors2):
        """Combine two factor dictionaries for LCM calculation."""
        combined = {}
        for prime in set(factors1.keys()).union(set(factors2.keys())):
            combined[prime] = max(factors1.get(prime, 0), factors2.get(prime, 0))
        return combined
    
    # Generate two random numbers with up to 5 digits
    number1 = random.randint(2, 99999)
    number2 = random.randint(2, 99999)
    
    # Factorize the numbers
    factors1 = factorize(number1)
    factors2 = factorize(number2)
    
    # Calculate the combined factors for LCM
    combined = combined_factors(factors1, factors2)
    
    # Calculate the LCM
    lcm_value = lcm(number1, number2)
    
    # Montando a expressão para a frente da carta
    front_text = f"<b>MMC</b><br>Ache o MMC dos números {number1} e {number2}"
    
    # Montando o texto para o verso da carta
    back_text = (f"<b>Desenvolvimento</b><br>"
                f"O mínimo múltiplo comum (MMC) corresponde ao menor número inteiro positivo, diferente de zero, que é múltiplo ao mesmo tempo de dois ou mais números<br><br>")

    factorization_steps = "<table border='1'>"
    
    n1, n2 = number1, number2
    divisor = 2
    while n1 > 1 or n2 > 1:
        if n1 % divisor == 0 or n2 % divisor == 0:
            factorization_steps += f"<tr><td>{n1 if n1 > 1 else '1'}</td><td>{n2 if n2 > 1 else '1'}</td><td> {divisor}</td></tr>"
            if n1 % divisor == 0:
                n1 //= divisor
            if n2 % divisor == 0:
                n2 //= divisor
        else:
            divisor += 1
    factorization_steps += "<tr><td>1</td><td>1</td></tr></table>"
    factorization_str = format_factors(combined)
    back_text += f"{factorization_steps}<br>O MMC entre {number1} e {number2} = {factorization_str} = {lcm_value}"
    
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