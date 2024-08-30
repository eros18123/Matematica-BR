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







def insert_prime_factorization_card(editor):

    front_text = ""
    back_text = ""

    def prime_factors(n):
        """Decompõe n em fatores primos e retorna uma lista de fatores."""
        factors = []
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1
            if divisor * divisor > n:
                if n > 1:
                    factors.append(n)
                break
        return factors
    
    # Exibir caixa de diálogo para inserir o número
    number, ok_pressed = QInputDialog.getInt(editor.parentWindow, "Digite o número", "Número:")

    # Verificar se o usuário pressionou OK e se o número é válido
    if ok_pressed and number > 1:
        # Texto para a frente da carta
        front_text = f"<b>Fatoração Numerica 2</b><br><font color='blue'>Faça a fatoração do número {number}?</font>"
        
        # Desenvolvimento do verso da carta
        factors = prime_factors(number)
        factor_table = "<table border='1'><tr><th>Número</th><th>Fator</th></tr>"
        current_value = number
        
        for factor in factors:
            factor_table += f"<tr><td>{current_value}</td><td>{factor}</td></tr>"
            current_value //= factor
        factor_table += f"<tr><td>{current_value}</td><td></td></tr></table><br>"
    
        multiplication_expression = " x ".join(map(str, factors))
        
        explanation_text = (
            f"<b>Desenvolvimento</b><br>"
            f"Abaixo faremos uma tabela com os possíveis números divisíveis do número {number}:<br><br>"
            f"{factor_table}"
            f"{multiplication_expression} = {number}<br>"
        )
    
        unique_factors = sorted(set(factors))
        unique_factors_text = ", ".join(map(str, unique_factors))
    
        # Ajuste na mensagem final com base nos fatores encontrados
        if len(factors) == 1:
            explanation_text += f"O número {number} não pode ser fatorado, pois ele só pode ser dividido por: 1 e ele mesmo ({number})."
        else:
            explanation_text += f"O número {number} pode ser fatorado por: 1, {unique_factors_text}."
    
        # Texto para o verso da carta
        back_text = explanation_text
    
        # Atualizando os campos na nota do editor
        #note = editor.note
        #note["Frente"] = front_text
        #note["Verso"] = back_text
        #editor.loadNote()
    #else:
        # Caso o usuário cancele ou insira um número inválido, não faz nada
        #pass






    # Definir front_text e back_text la em cima com um valor padrão


    front_texts = front_text
    
    # Obter os campos da nota atual
    note = editor.note
    field_names = list(note.keys())
    
    # Atualizar o primeiro campo com front_text
    if field_names:
        note[field_names[0]] = front_texts
    else:
        pass
    

    # Atualizar o segundo campo com back_text
    back_texts = back_text
    if len(field_names) > 1:
        note[field_names[1]] = back_texts
    else:
        pass
    
    # Iterar sobre os campos e atualizar cada um deles com valores genéricos
    for i, field_name in enumerate(field_names):
        if i not in [0, 1]:
            note[field_name] = f"Valor do campo {field_name}"
        else:
            pass
    
    editor.loadNote()


