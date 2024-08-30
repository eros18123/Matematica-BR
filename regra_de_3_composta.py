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


def insert_regra_composta(editor):
    # Gerar números aleatórios para a expressão
    artesas_1 = random.randint(1, 10)
    bonecas_1 = random.randint(1, 20)
    dias_1 = random.randint(1, 30)
    
    artesas_2 = random.randint(1, 10)
    dias_2 = random.randint(1, 30)
    
    # Garantir que a quantidade de bonecas 2 não é negativa
    while True:
        bonecas_2 = (bonecas_1 * artesas_2 * dias_2) / (artesas_1 * dias_1)
        if bonecas_2 > 0:
            bonecas_2 = int(bonecas_2)
            break
    
    # Montando a expressão para a frente da carta
    front_text = (f"<b>Regra de 3 Composta</b><br><font color='blue'>Em uma oficina de artesanato, {artesas_1} artesãs produzem {bonecas_1} bonecas de pano em {dias_1} dias. "
                  f"Se {artesas_2} artesãs trabalharem por {dias_2} dias, quantas bonecas serão produzidas?</font>")
    
    # Montando o texto para o verso da carta
    back_text = (f"<b>Desenvolvimento</b><br>"
                 f"1º passo: Criar uma tabela com as grandezas e analisar os dados.<br>"
                 f"<table border='1'>"
                 f"<tr><th>Número de artesãs</th><th>Dias trabalhados</th><th>Bonecas produzidas</th></tr>"
                 f"<tr><td>A</td><td>B</td><td>C</td></tr>"
                 f"<tr><td>{artesas_1}</td><td>{dias_1}</td><td>{bonecas_1}</td></tr>"
                 f"<tr><td>{artesas_2}</td><td>{dias_2}</td><td>X</td></tr>"
                 f"</table><br>"
                 f"Através da tabela, podemos notar que:<br>"
                 f"A e C são diretamente proporcionais: quanto maior o número de artesãs, mais bonecas serão produzidas.<br>"
                 f"B e C são diretamente proporcionais: quanto mais dias trabalhados, um maior número de bonecas serão produzidas.<br><br>"
                 f"2º passo: Encontrar o valor de x.<br>"
                 f"Observe que as grandezas A e B são diretamente proporcionais à grandeza C. "
                 f"Logo, o produto dos valores de A e B é proporcional aos valores de C.<br><br>"
                 f"{artesas_1}/{artesas_2} . {dias_1}/{dias_2} = {bonecas_1}/x<br>"
                 f"{artesas_1 * dias_1} / {artesas_2 * dias_2} = {bonecas_1} / x<br>"
                 #f"{artesas_1 * dias_1 * bonecas_2} = {artesas_2 * dias_2 * bonecas_1}<br>"
                 f"x = {artesas_2 * dias_2 * bonecas_1} / {artesas_1 * dias_1}<br>"
                 f"x = {bonecas_2}<br><br>"
                 f"Assim, serão produzidas {bonecas_2} bonecas.")
    
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