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

#from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QFileDialog, QInputDialog
#from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QFileDialog, QInputDialog, QMessageBox, QApplication, QMainWindow, QMenu, QAction
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QFileDialog, QInputDialog, QMessageBox
from PyQt6.QtGui import QPixmap, QFont, QIcon
from PyQt6.QtCore import Qt
from aqt import gui_hooks, mw



from PyQt6.QtWidgets import *

from PyQt6.QtWidgets import QDialog, QFrame, QVBoxLayout

import unicodedata  # Importar unicodedata para normalização de texto






class CustomDialogs(QDialog):
    def __init__(self, editor):
        super().__init__(None, Qt.WindowType.Window | Qt.WindowType.WindowMinimizeButtonHint | Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowTitle("Exercicios")

        self.setMinimumSize(500, 700)
        self.setGeometry(800, 100, 400, 300)  # Definir a geometria inicial (direita, baixo, largura, altura)

        # Crie um QFrame para a borda 3D
        outer_frame = QFrame(self)
        outer_frame.setStyleSheet("background-color: #FFFFE0; color: black;")
        outer_frame.setFrameShape(QFrame.Shape.Box)
        outer_frame.setFrameShadow(QFrame.Shadow.Raised)
        outer_frame.setLineWidth(3)
        outer_layout = QVBoxLayout(outer_frame)
        outer_layout.setContentsMargins(0, 0, 0, 0)  # Remove margens internas do frame

        # Layout vertical para colocar widgets
        inner_widget = QWidget()
        layout = QVBoxLayout(inner_widget)
        outer_layout.addWidget(inner_widget)


        # Adicionar uma área de rolagem
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(scroll_content)
        self.scroll_area.setWidget(scroll_content)
        layout.addWidget(self.scroll_area)

        # Layout horizontal para caixa de pesquisa
        search_layout = QHBoxLayout()
        layout.addLayout(search_layout)

        # Caixa de texto para pesquisa
        self.search_textbox = QLineEdit()
        font = QFont()
        font.setPointSize(22)
        self.search_textbox.setFont(font)
        self.search_textbox.setStyleSheet("border: 2px solid black;")
        search_layout.addWidget(self.search_textbox)

        # Botão de pesquisa
        self.search_button = QPushButton("Pesquisar")
        font_button = QFont()
        font_button.setPointSize(18)  # Tamanho da fonte do botão
        self.search_button.setFont(font_button)
        self.search_button.setStyleSheet("background-color: #8BC34A; height: 36px; color: black;")  # Ajuste de tamanho do botão
        search_layout.addWidget(self.search_button)

        # Conectar o sinal clicked do botão de pesquisa ao método on_search_clicked
        self.search_button.clicked.connect(self.on_search_clicked)



        # Adicionar o outer_frame ao layout principal do diálogo
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(outer_frame)









    # Caminho completo para o arquivo math.txt dentro da pasta do addon
        addon_folder = os.path.dirname(__file__)  # Diretório onde este arquivo Python está localizado (addon)
        file_path = os.path.join(addon_folder, "math.txt")

    # Verificar conteúdo do arquivo math.txt
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                lines = file.readlines()

            # Exibir o conteúdo do arquivo na caixa de diálogo
                label_content = QLabel("Escolha uma ação:")
                label_content.setStyleSheet("font-size: 25px;")  # Definir tamanho da fonte para 18px
                self.scroll_layout.addWidget(label_content)

                # Dicionário para armazenar botões criados
                self.button_dict = {}


            # Criar botões para cada linha de conteúdo

                for i, line in enumerate(lines, start=1):
                #for line in lines:
                    content = line.strip()
                    if content == "potenciacao":
                        try:
                        # Importar a função do arquivo potenciacao.py
                            from .potenciacao import insert_produto_potenciacao
                            button_execute = QPushButton(f"{i}-Potenciação (Ctrl+Alt+C)")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_produto_potenciacao(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Potenciação")] = button_execute

                            # Atalho de teclado Ctrl+Alt+C para potenciação
                            shortcut = QShortcut(QKeySequence("Ctrl+Alt+C"), self)
                            shortcut.activated.connect(lambda: insert_produto_potenciacao(editor))


                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar potenciacao.py: {e}")
                            self.scroll_layout.addWidget(error_label)

                    elif content == "algoritmo_da_divisao":
                        try:
                        # Importar a função do arquivo algoritmo_da_divisao.py
                            from .algoritmo_da_divisao import insert_divisao_algoritmo
                            button_execute = QPushButton(f"{i}-Algoritmo de Divisão (Ctrl+Alt+T)")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_divisao_algoritmo(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Algoritmo da Divisão")] = button_execute


                            # Atalho de teclado Ctrl+Alt+T para potenciação
                            shortcut = QShortcut(QKeySequence("Ctrl+Alt+T"), self)
                            shortcut.activated.connect(lambda: insert_divisao_algoritmo(editor))

                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar algoritmo_da_divisao.py: {e}")
                            self.scroll_layout.addWidget(error_label)




                    elif content == "analise_combinatoria_arranjo_simples":
                        try:
                        # Importar a função do arquivo analise_combinatoria_arranjo_simples.py
                            from .analise_combinatoria_arranjo_simples import insert_arrangement
                            button_execute = QPushButton(f"{i}-Análise Combinatória Arranjo Simples")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_arrangement(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Análise Combinatória Arranjo Simples")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar analise_combinatoria_arranjo_simples.py: {e}")
                            self.scroll_layout.addWidget(error_label)













                    elif content == "analise_combinatoria_permutacao_simples":
                        try:
                        # Importar a função do arquivo analise_combinatoria_permutacao_simples.py
                            from .analise_combinatoria_permutacao_simples import insert_permutation_simple
                            button_execute = QPushButton(f"{i}-Análise Combinatória Permutação Simples")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_permutation_simple(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Análise Combinatória Permutação Simples")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar analise_combinatoria_permutacao_simples.py: {e}")
                            self.scroll_layout.addWidget(error_label)

                    elif content == "conjuntos_inteiros1":
                        try:
                        # Importar a função do arquivo conjuntos_inteiros1.py
                            from .conjuntos_inteiros1 import insert_integer_number
                            button_execute = QPushButton(f"{i}-Conjuntos Inteiros Z")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_integer_number(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Inteiros Z")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_inteiros1.py: {e}")
                            self.scroll_layout.addWidget(error_label)

                    elif content == "conjuntos_inteiros2":
                        try:
                        # Importar a função do arquivo conjuntos_inteiros2.py
                            from .conjuntos_inteiros2 import insert_nonzero_integer_number
                            button_execute = QPushButton(f"{i}-Conjuntos Inteiros Z Não Nulos")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_nonzero_integer_number(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Inteiros Z Não Nulos")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_inteiros2.py: {e}")
                            self.scroll_layout.addWidget(error_label)

                    elif content == "conjuntos_inteiros3":
                        try:
                        # Importar a função do arquivo conjuntos_inteiros3.py
                            from .conjuntos_inteiros3 import insert_nonnegative_integer_number
                            button_execute = QPushButton(f"{i}-Conjuntos Inteiros Z Não Negativos")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_nonnegative_integer_number(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Inteiros Z Não Negativos")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_inteiros3.py: {e}")
                            self.scroll_layout.addWidget(error_label)

                    elif content == "conjuntos_inteiros4":
                        try:
                        # Importar a função do arquivo conjuntos_inteiros4.py
                            from .conjuntos_inteiros4 import insert_nonpositive_integer_number
                            button_execute = QPushButton(f"{i}-Conjuntos Inteiros Z Não Positivos")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_nonpositive_integer_number(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Inteiros Z Não Positivos")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_inteiros4.py: {e}")
                            self.scroll_layout.addWidget(error_label)

                    elif content == "conjuntos_inteiros5":
                        try:
                        # Importar a função do arquivo conjuntos_inteiros5.py
                            from .conjuntos_inteiros5 import insert_positive_nonzero_integer_number
                            button_execute = QPushButton(f"{i}-Conjuntos Inteiros Z Positivos e sem Zero")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_positive_nonzero_integer_number(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Inteiros Z Positivos e sem Zero")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_inteiros5.py: {e}")
                            self.scroll_layout.addWidget(error_label)

                    elif content == "conjuntos_inteiros6":
                        try:
                        # Importar a função do arquivo conjuntos_inteiros6.py
                            from .conjuntos_inteiros6 import insert_negative_nonzero_integer_number
                            button_execute = QPushButton(f"{i}-Conjuntos Inteiros Z Negativos e sem Zero")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_negative_nonzero_integer_number(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Inteiros Z Negativos e sem Zero")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_inteiros6.py: {e}")
                            self.scroll_layout.addWidget(error_label)

                    elif content == "conjuntos_irracionais":
                        try:
                        # Importar a função do arquivo conjuntos_irracionais.py
                            from .conjuntos_irracionais import insert_irrational_number
                            button_execute = QPushButton(f"{i}-Conjuntos Irracionais I")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_irrational_number(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Irracionais I")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_irracionais.py: {e}")
                            self.scroll_layout.addWidget(error_label)

                    elif content == "conjuntos_naturais1":
                        try:
                        # Importar a função do arquivo conjuntos_naturais1.py
                            from .conjuntos_naturais1 import insert_natural_number
                            button_execute = QPushButton(f"{i}-Conjuntos Naturais N")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_natural_number(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Naturais N")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_naturais1.py: {e}")
                            self.scroll_layout.addWidget(error_label)

                    elif content == "conjuntos_naturais2":
                        try:
                        # Importar a função do arquivo conjuntos_naturais2.py
                            from .conjuntos_naturais2 import insert_no_null_natural_number
                            button_execute = QPushButton(f"{i}-Conjuntos Naturais N Não Nulos")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_no_null_natural_number(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Naturais N Não Nulos")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_naturais2.py: {e}")
                            self.scroll_layout.addWidget(error_label)












###########################################################








                    elif content == "conjuntos_naturais3":
                        try:
                        # Importar a função do arquivo conjuntos_naturais3.py
                            from .conjuntos_naturais3 import insert_numeros_naturais_pares
                            button_execute = QPushButton(f"{i}-Conjuntos Naturais Pares")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_numeros_naturais_pares(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Naturais Pares")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_naturais3.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "conjuntos_naturais4":
                        try:
                        # Importar a função do arquivo conjuntos_naturais4.py
                            from .conjuntos_naturais4 import insert_natural_odd
                            button_execute = QPushButton(f"{i}-Conjuntos Naturais N Impares")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_natural_odd(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Naturais N Impares")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_naturais4.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "conjuntos_propriedades":
                        try:
                        # Importar a função do arquivo conjuntos_propriedades.py
                            from .conjuntos_propriedades import insert_properties_of_number_sets
                            button_execute = QPushButton(f"{i}-Conjuntos Propriedades")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_properties_of_number_sets(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Propriedades")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_propriedades.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "conjuntos_racionais1":
                        try:
                        # Importar a função do arquivo conjuntos_racionais1.py
                            from .conjuntos_racionais1 import insert_rational_number
                            button_execute = QPushButton(f"{i}-Conjuntos Racionais Q")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_rational_number(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Racionais Q")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_racionais1.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "conjuntos_racionais2":
                        try:
                        # Importar a função do arquivo conjuntos_racionais2.py
                            from .conjuntos_racionais2 import insert_nonzero_rational_number
                            button_execute = QPushButton(f"{i}-Conjuntos Racionais Q Não Nulos")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_nonzero_rational_number(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Racionais Q Não Nulos")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_racionais2.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "conjuntos_reais_e_complexos":
                        try:
                        # Importar a função do arquivo conjuntos_reais_e_complexos.py
                            from .conjuntos_reais_e_complexos import insert_real
                            button_execute = QPushButton(f"{i}-Conjuntos Reais e Complexos")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_real(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Conjuntos Reais e Complexos")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar conjuntos_reais_e_complexos.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "divisibilidade_3":
                        try:
                        # Importar a função do arquivo divisibilidade_3.py
                            from .divisibilidade_3 import insert_div_3
                            button_execute = QPushButton(f"{i}-Divisibilidade por 3")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_div_3(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Divisibilidade por 3")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar divisibilidade_3.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "divisibilidade_4":
                        try:
                        # Importar a função do arquivo divisibilidade_4.py
                            from .divisibilidade_4 import insert_div_4
                            button_execute = QPushButton(f"{i}-Divisibilidade por 4")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_div_4(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Divisibilidade por 4")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar divisibilidade_4.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "divisibilidade_6":
                        try:
                        # Importar a função do arquivo divisibilidade_6.py
                            from .divisibilidade_6 import insert_div_6
                            button_execute = QPushButton(f"{i}-Divisibilidade por 6")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_div_6(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Divisibilidade por 6")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar divisibilidade_6.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "divisibilidade_7":
                        try:
                        # Importar a função do arquivo divisibilidade_7.py
                            from .divisibilidade_7 import insert_div_7
                            button_execute = QPushButton(f"{i}-Divisibilidade por 7")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_div_7(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Divisibilidade por 7")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar divisibilidade_7.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "divisibilidade_8":
                        try:
                        # Importar a função do arquivo divisibilidade_8.py
                            from .divisibilidade_8 import insert_div_8
                            button_execute = QPushButton(f"{i}-Divisibilidade por 8")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_div_8(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Divisibilidade por 8")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar divisibilidade_8.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "divisibilidade_9":
                        try:
                        # Importar a função do arquivo divisibilidade_9.py
                            from .divisibilidade_9 import insert_div_9
                            button_execute = QPushButton(f"{i}-Divisibilidade por 9")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_div_9(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Divisibilidade por 9")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar divisibilidade_9.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "dizima_periodica":
                        try:
                        # Importar a função do arquivo dizima_periodica.py
                            from .dizima_periodica import insert_repeating_decimal
                            button_execute = QPushButton(f"{i}-Dízima Periódica")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_repeating_decimal(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Dízima Periódica")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar dizima_periodica.py: {e}")
                            self.scroll_layout.addWidget(error_label)

                    elif content == "fatoracao":
                        try:
                        # Importar a função do arquivo fatoracao.py
                            from .fatoracao import insert_prime_factorization
                            button_execute = QPushButton(f"{i}-Fatoração")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_prime_factorization(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Fatoração")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar fatoracao.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "fatoracao_digitar":
                        try:
                        # Importar a função do arquivo fatoracao_digitar.py
                            from .fatoracao_digitar import insert_prime_factorization_card
                            button_execute = QPushButton(f"{i}-Fatoração - Digitar")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_prime_factorization_card(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Fatoração - Digitar")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar fatoracao_digitar.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "intervalos_abertos":
                        try:
                        # Importar a função do arquivo intervalos_abertos.py
                            from .intervalos_abertos import insert_numeric_interval_aberto
                            button_execute = QPushButton(f"{i}-Intervalos Abertos")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_numeric_interval_aberto(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Intervalos Abertos")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar intervalos_abertos.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "intervalos_fechados":
                        try:
                        # Importar a função do arquivo intervalos_fechados.py
                            from .intervalos_fechados import insert_numeric_interval_fechado
                            button_execute = QPushButton(f"{i}-Intervalos Fechados")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_numeric_interval_fechado(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Intervalos Fechados")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar intervalos_fechados.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "juros_compostos":
                        try:
                        # Importar a função do arquivo juros_compostos.py
                            from .juros_compostos import insert_compound_interest
                            button_execute = QPushButton(f"{i}-Juros Compostos")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_compound_interest(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Juros Compostos")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar juros_compostos.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "juros_simples":
                        try:
                        # Importar a função do arquivo juros_simples.py
                            from .juros_simples import insert_simple_interest
                            button_execute = QPushButton(f"{i}-Juros Simples")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_simple_interest(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Juros Simples")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar juros_simples.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "mdc":
                        try:
                        # Importar a função do arquivo mdc.py
                            from .mdc import insert_mdc
                            button_execute = QPushButton(f"{i}-MDC - Máximo Divisor Comum")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_mdc(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("MDC - Máximo Divisor Comum")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar mdc.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "media_aritmetica_ponderada":
                        try:
                        # Importar a função do arquivo media_aritmetica_ponderada.py
                            from .media_aritmetica_ponderada import insert_media_aritmetica_ponderada
                            button_execute = QPushButton(f"{i}-Média Aritmética Ponderada")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_media_aritmetica_ponderada(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Média Aritmética Ponderada")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar media_aritmetica_ponderada.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "media_aritmetica_simples":
                        try:
                        # Importar a função do arquivo media_aritmetica_simples.py
                            from .media_aritmetica_simples import insert_media_aritmetica_simples
                            button_execute = QPushButton(f"{i}-Média Aritmética Simples")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_media_aritmetica_simples(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("MMédia Aritmética Simples")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar media_aritmetica_simples.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "mmc1":
                        try:
                        # Importar a função do arquivo mmc1.py
                            from .mmc1 import insert_mmc1
                            button_execute = QPushButton(f"{i}-MMC - Mínimo Múltiplo Comum")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_mmc1(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("MMC - Mínimo Múltiplo Comum")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar mmc1.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "numeros_primos1":
                        try:
                        # Importar a função do arquivo numeros_primos1.py
                            from .numeros_primos1 import insert_prime_number
                            button_execute = QPushButton(f"{i}-Números Primos 1")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_prime_number(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Números Primos 1")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar numeros_primos1.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "numeros_primos2":
                        try:
                        # Importar a função do arquivo numeros_primos2.py
                            from .numeros_primos2 import insert_prime_check
                            button_execute = QPushButton(f"{i}-Números Primos 2")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_prime_check(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Números Primos 2")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar numeros_primos2.py: {e}")
                            self.scroll_layout.addWidget(error_label)


################ pula potenciacao pq ele é o primeiro

                    elif content == "potenciacao_fracao":
                        try:
                        # Importar a função do arquivo potenciacao_fracao.py
                            from .potenciacao_fracao import insert_produto_potenciacao_fracao
                            button_execute = QPushButton(f"{i}-Potenciação - Fração")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_produto_potenciacao_fracao(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Potenciação - Fração")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar potenciacao_fracao.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "prodnotaveis_cubo_diferenca":
                        try:
                        # Importar a função do arquivo prodnotaveis_cubo_diferenca.py
                            from .prodnotaveis_cubo_diferenca import insert_cubo_diferenca
                            button_execute = QPushButton(f"{i}-Produtos Notáveis - Cubo da Diferença")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_cubo_diferenca(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Produtos Notáveis - Cubo da Diferença")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar prodnotaveis_cubo_diferenca.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "prodnotaveis_cubo_soma":
                        try:
                        # Importar a função do arquivo prodnotaveis_cubo_soma.py
                            from .prodnotaveis_cubo_soma import insert_cubo_soma
                            button_execute = QPushButton(f"{i}-Produtos Notáveis - Cubo da Soma")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_cubo_soma(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Produtos Notáveis - Cubo da Soma")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar prodnotaveis_cubo_soma.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "prodnotaveis_produto_soma_diferenca":
                        try:
                        # Importar a função do arquivo prodnotaveis_produto_soma_diferenca.py
                            from .prodnotaveis_produto_soma_diferenca import insert_produto_soma_diferenca
                            button_execute = QPushButton(f"{i}-Produtos Notáveis - Produto da Soma pela Diferença")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_produto_soma_diferenca(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Produtos Notáveis - Produto da Soma pela Diferença")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar prodnotaveis_produto_soma_diferenca.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "prodnotaveis_quadrado_diferenca":
                        try:
                        # Importar a função do arquivo prodnotaveis_quadrado_diferenca.py
                            from .prodnotaveis_quadrado_diferenca import insert_quadrado_diferenca
                            button_execute = QPushButton(f"{i}-Produtos Notáveis - Quadrado da Diferença")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_quadrado_diferenca(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Produtos Notáveis - Quadrado da Diferença")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar prodnotaveis_quadrado_diferenca.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "prodnotaveis_quadrado_soma":
                        try:
                        # Importar a função do arquivo prodnotaveis_quadrado_soma.py
                            from .prodnotaveis_quadrado_soma import insert_quadrado_soma
                            button_execute = QPushButton(f"{i}-Produtos Notáveis - Quadrado da Soma")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_quadrado_soma(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Produtos Notáveis - Quadrado da Soma")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar prodnotaveis_quadrado_soma.py: {e}")
                            self.scroll_layout.addWidget(error_label)



                    elif content == "regra_de_3_composta":
                        try:
                        # Importar a função do arquivo regra_de_3_composta.py
                            from .regra_de_3_composta import insert_regra_composta
                            button_execute = QPushButton(f"{i}-Regra de 3 Composta")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_regra_composta(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Regra de 3 Composta")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar regra_de_3_composta.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "regra_de_3_simples_distancia":
                        try:
                        # Importar a função do arquivo regra_de_3_simples_distancia.py
                            from .regra_de_3_simples_distancia import insert_rule_of_three_simple_time
                            button_execute = QPushButton(f"{i}-Regra de 3 Simples - Distância")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_rule_of_three_simple_time(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Regra de 3 Simples - Distância")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar regra_de_3_simples_distancia.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "regra_de_3_simples_massa":
                        try:
                        # Importar a função do arquivo regra_de_3_simples_massa.py
                            from .regra_de_3_simples_massa import insert_rule_of_three_simple
                            button_execute = QPushButton(f"{i}-Regra de 3 Simples - Massa")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_rule_of_three_simple(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Regra de 3 Simples - Massa")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar regra_de_3_simples_massa.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "sistemas_de_numeracao_classe":
                        try:
                        # Importar a função do arquivo sistemas_de_numeracao_classe.py
                            from .sistemas_de_numeracao_classe import insert_sistemas_numeracao2
                            button_execute = QPushButton(f"{i}-Sistemas de Numeração - Classe")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_sistemas_numeracao2(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Sistemas de Numeração - Classe")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar sistemas_de_numeracao_classe.py: {e}")
                            self.scroll_layout.addWidget(error_label)


                    elif content == "sistemas_de_numeracao_representacao_numerica":
                        try:
                        # Importar a função do arquivo sistemas_de_numeracao_representacao_numerica.py
                            from .sistemas_de_numeracao_representacao_numerica import insert_sistemas_numeracao
                            button_execute = QPushButton(f"{i}-Sistemas de Numeração - Representação Númerica")
                            button_execute.setStyleSheet("font-size: 19px; background-color: lightblue;")  # Estilizar o botão
                            button_execute.clicked.connect(lambda _, editor=editor: insert_sistemas_numeracao(editor))
                            self.scroll_layout.addWidget(button_execute)
                            self.button_dict[normalize_text("Sistemas de Numeração - Representação Númerica")] = button_execute
                        except ImportError as e:
                            error_label = QLabel(f"Erro ao importar sistemas_de_numeracao_representacao_numerica.py: {e}")
                            self.scroll_layout.addWidget(error_label)









#############################################################


                
        else:
            label = QLabel("Arquivo math.txt não encontrado.")
            self.scroll_layout.addWidget(label)



        # Estilizar o fundo da caixa de diálogo
        self.setStyleSheet("background-color: white; color: black;")

        # Conectar a função de pesquisa ao botão
        #self.search_button.clicked.connect(lambda: self.on_search_clicked(self.search_textbox.text()))





    def on_search_clicked(self):
        search_text = self.search_textbox.text()
        if search_text:
            search_text_normalized = normalize_text(search_text)
            buttons_to_highlight = []

            for key in self.button_dict.keys():
                if search_text_normalized in key:
                    buttons_to_highlight.append(key)

            if buttons_to_highlight:
                for button in self.button_dict.values():
                    button.setStyleSheet("font-size: 19px; background-color: lightblue; color: black;")

                for key in buttons_to_highlight:
                    button = self.button_dict[key]
                    button.setStyleSheet("font-size: 19px; background-color: yellow; color: black;")
                    self.scroll_area.ensureWidgetVisible(button)
            else:
                for button in self.button_dict.values():
                    button.setStyleSheet("font-size: 19px; background-color: lightblue; color: black;")
                QMessageBox.information(self, "Botão não encontrado", f"Não existe nenhum botão com o nome '{search_text}'.")




        else:
            for button in self.button_dict.values():
                button.setStyleSheet("font-size: 19px; background-color: lightblue; color: black;")
            QMessageBox.information(self, "Campo vazio", "Por favor, digite o nome de um botão para pesquisar.")





def normalize_text(text):
    # Função para normalizar o texto removendo acentos e convertendo para minúsculas
    normalized = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII').lower()
    return normalized.replace(" ", "_")

  

##################################################################################################################################################################################################################### Final do botao Matematica

#    math_button = editor.addButton(
#        icon=None,
#        cmd="math-menu",
#        func=lambda editor=editor: math_menu.exec(QCursor.pos()),
#        tip="Operações Matemáticas",
#        #label="<b>Matemática</b>",

#        label=create_button_label1("Matematica", "yellow", "black", "bold"),
#        keys="Ctrl+M"
#    )
#    buttons.append(math_button)
#    return buttons


#def create_button_label1(text: str, background_color: str, text_color: str, font_weight: str) -> str:
#    return f"<span style='background-color:{background_color};color:{text_color};font-weight:{font_weight};'>{text}</span>"



