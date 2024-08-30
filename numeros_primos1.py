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





def insert_prime_number(editor):
    def is_prime(n):
        """Retorna True se n for um número primo, caso contrário, False."""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def generate_random_prime():
        """Gera um número primo aleatório com até 5 dígitos."""
        while True:
            num = random.randint(2, 99999)
            if is_prime(num):
                return num

    def generate_random_non_prime():
        """Gera um número não primo aleatório com até 5 dígitos."""
        while True:
            num = random.randint(2, 99999)
            if not is_prime(num):
                return num

    def find_divisors(n):
        """Encontra todos os divisores de n."""
        divisors = [i for i in range(2, n) if n % i == 0]
        return divisors

    # Decidir se será um número primo ou não primo (50% de chance para cada)
    if random.choice([True, False]):
        number = generate_random_prime()
        is_prime_number = True
    else:
        number = generate_random_non_prime()
        is_prime_number = False
    
    # Texto para a frente da carta
    front_text = f"<b>Numeros Primos 1</b><br><font color='blue'>Diga se o número {number} é primo ou não?</font>"
    
    # Desenvolvimento do verso da carta
    explanation_text = (
        "<b>Desenvolvimento</b><br>"
        "Os números primos são números naturais maiores que 1 e possuem apenas 2 divisores (1 e ele mesmo).<br>"
        "Condições:<br>"
        "- O número 1 é o único número ímpar que não é primo.<br>"
        "- O número 2 é o único número primo que é par.<br>"
        "- O número 5 é o único número primo que termina com 5.<br>"
        "- Todos os outros números primos terminam com 1, 3, 7 e 9.<br>"
        "Entre 1 e 100, há 25 números primos: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 e 97.<br>"
    )

    if is_prime_number:
        explanation = f"Sim, o número {number} é primo pois ele possui apenas dois divisores: 1 e ele mesmo."
    else:
        divisors = find_divisors(number)
        explanation = f"Não, o número {number} não é primo pois ele pode ser dividido por: {', '.join(map(str, divisors))}."

    # Texto para o verso da carta
    back_text = f"{explanation_text}<br>{explanation}"

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