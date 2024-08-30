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




def insert_sistemas_numeracao(editor):
    # Definindo as probabilidades de cada faixa de dígitos
    digit_probs = {
        9: 0.01,   # 1% de probabilidade para números com 9 dígitos
        8: 0.05,   # 5% de probabilidade para números com 8 dígitos
        7: 0.10,   # 10% de probabilidade para números com 7 dígitos
        6: 0.15,   # 15% de probabilidade para números com 6 dígitos
        5: 0.20,   # 20% de probabilidade para números com 5 dígitos
        4: 0.20,   # 20% de probabilidade para números com 4 dígitos
        3: 0.20,   # 20% de probabilidade para números com 3 dígitos
        2: 0.05,   # 5% de probabilidade para números com 2 dígitos
        1: 0.05    # 5% de probabilidade para números com 1 dígito
    }
    
    # Escolhendo aleatoriamente o número de dígitos baseado nas probabilidades
    num_digits = random.choices(list(digit_probs.keys()), weights=digit_probs.values())[0]
    
    # Gerando um número aleatório com o número de dígitos escolhido
    if num_digits == 1:
        numero = random.randint(0, 9)
    else:
        min_number = 10 ** (num_digits - 1)
        max_number = (10 ** num_digits) - 1
        numero = random.randint(min_number, max_number)
    
    # Formatar número com pontos
    numero_formatado = f"{numero:,}".replace(',', '.')

    # Separar as classes
    unidades = numero % 1000
    milhares = (numero // 1000) % 1000
    milhoes = (numero // 1000000) % 1000
    
    # Formatar as classes com pontos
    unidades_formatado = f"{unidades:,}".replace(',', '.')
    milhares_formatado = f"{milhares:,}".replace(',', '.')
    milhoes_formatado = f"{milhoes:,}".replace(',', '.')
    
    # Descrição dos dígitos
    descricao_digitos = [
        (numero % 10, f"{numero % 10} unidades"),
        ((numero // 10) % 10, f"{((numero // 10) % 10) * 10} unidades ou {((numero // 10) % 10)} dezenas"),
        ((numero // 100) % 10, f"{((numero // 100) % 10) * 100} unidades ou {((numero // 100) % 10)} centenas"),
        ((numero // 1000) % 10, f"{((numero // 1000) % 10) * 1000} unidades ou {((numero // 1000) % 10)} unidades de milhares"),
        ((numero // 10000) % 10, f"{((numero // 10000) % 10) * 10000} unidades ou {((numero // 10000) % 10)} dezenas de milhares"),
        ((numero // 100000) % 10, f"{((numero // 100000) % 10) * 100000} unidades ou {((numero // 100000) % 10)} centenas de milhares"),
        ((numero // 1000000) % 10, f"{((numero // 1000000) % 10) * 1000000} unidades ou {((numero // 1000000) % 10)} unidades de milhões"),
        ((numero // 10000000) % 10, f"{((numero // 10000000) % 10) * 10000000} unidades ou {((numero // 10000000) % 10)} dezenas de milhões"),
        ((numero // 100000000) % 10, f"{((numero // 100000000) % 10) * 100000000} unidades ou {((numero // 100000000) % 10)} centenas de milhões")
    ]
    
    descricao_digitos = list(reversed(descricao_digitos)) # Reverter a lista para começar do dígito mais significativo
    
    # Remover os zeros à esquerda
    while descricao_digitos and descricao_digitos[0][0] == 0:
        descricao_digitos.pop(0)
    
    # Montando a expressão para a frente da carta
    front_text = (f"<b>Sistema de Numeração - Representação</b><br><font color='blue'>Como representar o número {numero_formatado} como sistema de numeração?</font>")
    
    # Montando o texto para o verso da carta
    back_text = (f"<b>Desenvolvimento</b><br>"
                 f"{numero_formatado}<br>"
                 f"<table border='1' cellpadding='5' cellspacing='0'>"
                 f"<tr><th style='text-align:center;'>Dígito</th><th style='text-align:center;'>Representação</th></tr>")
    
    for i in range(len(descricao_digitos)):
        digito, descricao = descricao_digitos[i]
        
        # Determinar a cor com base nas regras fornecidas
        if i >= len(descricao_digitos) - 3:
            cor = "red"  # Últimas 3 linhas são vermelhas (unidades simples)
        elif i >= len(descricao_digitos) - 6:
            cor = "green"  # Linhas acima das últimas 3, se houver, são verdes (milhares)
        else:
            cor = "black"  # Restante é preto
        
        back_text += f"<tr><td style='text-align:center; color:{cor};'>{digito}</td><td style='text-align:left; color:{cor};'>{descricao}</td></tr>"
    
    back_text += ("</table><br>"
                  f"1 algarismo = 1 ordem<br>"
                  f"começa da direita pra esquerda <-<br>"
                  f"3 ordens = 1 classe<br><br>"
                  f"Veja a tabela:<br>"
                  f"<table border='1' cellpadding='5' cellspacing='0'>"
                  f"<tr><th colspan='9' style='text-align:center;'>Classes</th></tr>"
                  f"<tr><th colspan='3' style='text-align:center;'>Milhões</th><th colspan='3' style='text-align:center;'>Milhares</th><th colspan='3' style='text-align:center;'>Unid. Simples</th></tr>"
                  f"<tr><th colspan='9' style='text-align:center;'>Ordens</th></tr>"
                  f"<tr><td style='text-align:center;'><font color='black'>{milhoes // 100}</font></td><td style='text-align:center;'><font color='black'>{(milhoes % 100) // 10}</font></td><td style='text-align:center;'><font color='black'>{milhoes % 10}</font></td>"
                  f"<td style='text-align:center;'><font color='green'>{milhares // 100}</font></td><td style='text-align:center;'><font color='green'>{(milhares % 100) // 10}</font></td><td style='text-align:center;'><font color='green'>{milhares % 10}</font></td>"
                  f"<td style='text-align:center;'><font color='red'>{unidades // 100}</font></td><td style='text-align:center;'><font color='red'>{(unidades % 100) // 10}</font></td><td style='text-align:center;'><font color='red'>{unidades % 10}</font></td></tr>"
                  f"</table><br>"
                  f"{numero_formatado}<br>"
                  f"<table border='1' cellpadding='5' cellspacing='0'>"
                  f"<tr><th style='text-align:center;'>Número</th><th style='text-align:center;'>Classe</th></tr>"
                  f"<tr><td style='text-align:center;'><font color='black'>{milhoes_formatado}</font></td><td style='text-align:left;'>Milhões</td></tr>"
                  f"<tr><td style='text-align:center;'><font color='green'>{milhares_formatado}</font></td><td style='text-align:left;'><font color='green'>Milhares</font></td></tr>"
                  f"<tr><td style='text-align:center;'><font color='red'>{unidades_formatado}</font></td><td style='text-align:left;'><font color='red'>Unidades Simples</font></td></tr>"

                  f"</table>")
   

    
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