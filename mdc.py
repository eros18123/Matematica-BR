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





def insert_mdc(editor):
    """Generate Anki card for MDC factorization."""
    
    def generate_numbers():
        while True:
            num1 = random.randint(2, 99999)
            num2 = random.randint(2, 99999)
            if math.gcd(num1, num2) > 1:
                if random.random() > 0.1:  # 90% chance of having a common divisor
                    return num1, num2
            else:
                if random.random() <= 0.1:  # 10% chance of having no common divisor
                    return num1, num2
    
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
    
    def gcd(a, b):
        """Calculate the Greatest Common Divisor (GCD) of two numbers."""
        return math.gcd(a, b)
    
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
        """Combine two factor dictionaries for GCD calculation."""
        combined = {}
        for prime in set(factors1.keys()).intersection(set(factors2.keys())):
            combined[prime] = min(factors1.get(prime, 0), factors2.get(prime, 0))
        return combined
    
    # Generate two random numbers
    number1, number2 = generate_numbers()
    
    # Factorize the numbers
    factors1 = factorize(number1)
    factors2 = factorize(number2)
    
    # Calculate the combined factors for GCD
    combined = combined_factors(factors1, factors2)
    
    # Calculate the GCD
    gcd_value = gcd(number1, number2)
    
    # Montando a expressão para a frente da carta
    front_text = f"<b>MDC</b><br>Ache o MDC dos números {number1} e {number2}"
    
    # Montando o texto para o verso da carta
    back_text = (f"<b>Desenvolvimento</b><br>"
                 f"O máximo divisor comum (MDC ou M.D.C) corresponde ao produto dos divisores comuns entre dois ou mais números inteiros.<br><br>")

    factorization_steps = "<table border='1'>"
    
    n1, n2 = number1, number2
    divisor = 2
    while n1 > 1 or n2 > 1:
        if n1 % divisor == 0 or n2 % divisor == 0:
            color = "red" if n1 % divisor == 0 and n2 % divisor == 0 else "black"
            bgcolor = "yellow" if n1 % divisor == 0 and n2 % divisor == 0 else "white"
            factorization_steps += f"<tr><td>{n1 if n1 > 1 else '1'}</td><td>{n2 if n2 > 1 else '1'}</td><td style='color: {color}; background-color: {bgcolor};'>{divisor}</td></tr>"
            if n1 % divisor == 0:
                n1 //= divisor
            if n2 % divisor == 0:
                n2 //= divisor
        else:
            divisor += 1
    factorization_steps += "<tr><td>1</td><td>1</td></tr></table>"
    factorization_str = format_factors(combined)
    back_text += f"{factorization_steps}<br>"
    
    if gcd_value == 1:
        back_text += f"Não existe MDC entre {number1} e {number2}"
    else:
        back_text += f"O MDC entre {number1} e {number2} = {factorization_str} = {gcd_value}"
    
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