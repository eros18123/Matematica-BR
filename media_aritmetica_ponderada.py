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






def insert_media_aritmetica_ponderada(editor):
    # Definindo as matérias
    materias = ["Matemática", "Português", "Geografia", "História", "Inglês"]
    
    # Determinando uma quantidade aleatória de matérias (entre 3 e 5)
    quantidade_materias = random.randint(3, 5)
    
    # Selecionando matérias aleatoriamente
    materias_selecionadas = random.sample(materias, quantidade_materias)
    
    # Gerando notas aleatórias de 1 a 10 com 1 decimal e pesos de 1 a 5
    notas = [round(random.uniform(1, 10), 1) for _ in range(quantidade_materias)]
    pesos = [random.randint(1, 5) for _ in range(quantidade_materias)]
    
    # Montando a tabela HTML para a frente da carta
    table_rows = "".join([f"<tr><td>{i+1}</td><td>{materia}</td><td>{nota}</td><td>{peso}</td></tr>" 
                          for i, (materia, nota, peso) in enumerate(zip(materias_selecionadas, notas, pesos))])
    front_text = (f"<b>Média Aritmética Ponderada</b><br><font color='blue'>Considerando as notas e os respectivos pesos de cada uma delas, indique qual a média que o aluno obteve no curso. </font><br><br>"
                  f"<table border='1'><tr><th>##</th><th>Matéria</th><th>Nota</th><th>Peso</th></tr>{table_rows}</table><br>")
                  #f"<font color='blue'>Qual a média que ele obteve no curso?</font>")
    
    # Calculando a média aritmética ponderada
    produtos = [round(nota * peso, 1) for nota, peso in zip(notas, pesos)]
    numerador = sum(produtos)
    denominador = sum(pesos)
    media_ponderada = round(numerador / denominador, 1)
    
    # Montando o texto para o verso da carta
    produtos_str = ' + '.join(f'{peso}.{str(nota).replace(".", ",")}' for nota, peso in zip(notas, pesos))
    pesos_str = ' + '.join(map(str, pesos))
    produtos_soma = ' + '.join(map(str, produtos))
    
    back_text = (f"<b>Desenvolvimento:</b><br>"
                 f"A Média Aritmética Ponderada é calculada multiplicando cada valor do conjunto de dados pelo seu peso.<br><br>"

                 f"Mp = (P1.X1+P2.X2+...PN.XN)/P1+P2+...PN<br>"

                 f"Onde,<br>"
                 f"Mp: Média aritmética ponderada<br>"
                 f"p1, p2,..., pn: pesos<br>"
                 f"x1, x2,...,xn: valores dos dados<br><br>"

                 f"Mp = ({produtos_str}) / {pesos_str}<br>"
                 f"Mp = ({produtos_soma}) / {denominador}<br>"
                 f"Mp = {round(numerador, 1)} / {denominador}<br>"
                 f"Mp = {media_ponderada}")
    
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
