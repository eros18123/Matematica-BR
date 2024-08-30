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





def insert_properties_of_number_sets(editor):
    # Definindo os conjuntos e embaralhando para misturar a ordem
    sets = ['N (naturais)', 'Z (inteiros)', 'Q (racionais)', 'I (irracionais)', 'R (reais)']
    random.shuffle(sets)
    
    # Pares de subconjuntos conforme especificado
    subset_pairs = [
        ('N (naturais)', 'Z (inteiros)'),
        ('N (naturais)', 'Q (racionais)'),
        ('N (naturais)', 'R (reais)'),
        ('Z (inteiros)', 'Q (racionais)'),
        ('Z (inteiros)', 'R (reais)'),
        ('Q (racionais)', 'R (reais)'),
        ('I (irracionais)', 'R (reais)'),
        ('N (naturais)', 'I (irracionais)'),
        ('Z (inteiros)', 'N (naturais)'),
        ('Z (inteiros)', 'I (irracionais)'),
        ('Q (racionais)', 'N (naturais)'),
        ('Q (racionais)', 'Z (inteiros)'),
        ('Q (racionais)', 'I (irracionais)'),
        ('I (irracionais)', 'N (naturais)'),
        ('I (irracionais)', 'Z (inteiros)'),
        ('I (irracionais)', 'Q (racionais)'),
        ('R (reais)', 'N (naturais)'),
        ('R (reais)', 'Z (inteiros)'),
        ('R (reais)', 'Q (racionais)'),
        ('R (reais)', 'I (irracionais)')
    ]
    
    # Escolhendo aleatoriamente um par de subconjuntos
    subset_pair = random.choice(subset_pairs)
    
    # Definindo as variáveis
    first_subset = subset_pair[0]
    second_subset = subset_pair[1]
    
    # Formatando o front do cartão
    front_text = f"<b>Propriedades dos Conjuntos</b><br><font color='blue'>Diga se {subset_pair[0]} é subconjunto de {subset_pair[1]}</font>"
    
    # Formatando o verso do cartão com a verificação e todas as relações de subconjuntos
    back_text = (
        f"<b>Desenvolvimento</b><br><br>"
        f"N (naturais) é subconjunto de Z (inteiros) -> N ⊆ Z<br>"
        f"N (naturais) é subconjunto de Q (racionais) -> N ⊆ Q<br>"
        f"N (naturais) é subconjunto de R (reais) -> N ⊆ R<br>"
        f"Z (inteiros) é subconjunto de Q (racionais) -> Z ⊆ Q<br>"
        f"Z (inteiros) é subconjunto de R (reais) -> Z ⊆ R<br>"
        f"Q (racionais) é subconjunto de R (reais) -> Q ⊆ R<br>"
        f"I (irracionais) é subconjunto de R (reais) -> I ⊆ R<br><br>"
    )
    
    # Verificando se o primeiro conjunto é subconjunto do segundo
    if (first_subset, second_subset) in [
        ('N (naturais)', 'Z (inteiros)'),
        ('N (naturais)', 'Q (racionais)'),
        ('N (naturais)', 'R (reais)'),
        ('Z (inteiros)', 'Q (racionais)'),
        ('Z (inteiros)', 'R (reais)'),
        ('Q (racionais)', 'R (reais)'),
        ('I (irracionais)', 'R (reais)')
    ]:
        back_text += f"Sim, {first_subset} é subconjunto de {second_subset}"
    else:
        back_text += f"Não, {first_subset} não é subconjunto de {second_subset}"
    
   





    # Update the fields in the editor's note
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





