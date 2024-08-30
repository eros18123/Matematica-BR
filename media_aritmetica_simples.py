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





def insert_media_aritmetica_simples(editor):
    # Definindo as matérias
    materias = ["Matemática", "Português", "Geografia", "História", "Inglês"]
    
    # Determinando uma quantidade aleatória de matérias (entre 3 e 5)
    quantidade_materias = random.randint(3, 5)
    
    # Selecionando matérias aleatoriamente
    materias_selecionadas = random.sample(materias, quantidade_materias)
    
    # Gerando notas aleatórias de 1 a 10 com 1 decimal
    notas = [round(random.uniform(1, 10), 1) for _ in range(quantidade_materias)]
    
    # Montando a tabela HTML para a frente da carta
    table_rows = "".join([f"<tr><td>{i+1}</td><td>{materia}</td><td>{nota}</td></tr>" 
                          for i, (materia, nota) in enumerate(zip(materias_selecionadas, notas))])
    front_text = (f"<b>Média Aritmética Simples</b><br><font color='blue'>Sabendo que as notas de um aluno foram: </font><br><br>"
                  f"<table border='1'><tr><th>##</th><th>Matéria</th><th>Nota</th></tr>{table_rows}</table><br>"
                  f"<font color='blue'>Qual a média que ele obteve no curso?</font>")
    
    # Calculando a média aritmética simples
    soma_notas = round(sum(notas), 1)
    media = round(soma_notas / len(notas), 1)
    
    # Montando o texto para o verso da carta
    back_text = (f"<b>Desenvolvimento:</b><br>"
                 f"A Média Aritmética de um conjunto de dados é obtida somando todos os valores e dividindo o valor encontrado pelo número de dados desse conjunto.<br><br>"

                 f"Ms = (X1+X2+X3+...Xn)/n<br>"
                 f"Onde,<br>"
                 f"Ms: Média aritmética simples<br>"
                 f"x1, x2, x3,...,xn: valores dos dados<br>"
                 f"n: número de dados<br>"

                 f"<br>Ms = ({' + '.join(map(str, notas))}) / {len(notas)}<br>"
                 f"Ms = {soma_notas} / {len(notas)}<br>"
                 f"Ms = {media}")
    
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
