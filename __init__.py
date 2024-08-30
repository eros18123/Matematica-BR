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





############################################################### ALGORITMO DA DIVISAO


# Importar a função do arquivo algoritmo_da_divisao.py
from .algoritmo_da_divisao import insert_divisao_algoritmo



# Função para criar o atalho
#def setup_shortcut(editor):
#    shortcut = QShortcut(QKeySequence("Ctrl+Alt+T"), editor.widget)
#    shortcut.activated.connect(lambda: insert_divisao_algoritmo(editor))

# Adicionar a configuração do atalho ao inicializar o editor
#def on_editor_created(editor):
#    setup_shortcut(editor)

# Registrando a função para quando o editor for criado
#gui_hooks.editor_did_init.append(on_editor_created)



#################################################### ANALISE COMBINATORIA ################

#PERMUTAÇAO
# Importar a função do arquivo analise_combinatoria_permutacao_simples.py
from .analise_combinatoria_permutacao_simples import insert_permutation_simple


#ARRANJO
# Importar a função do arquivo analise_combinatoria_arranjo_simples.py
from .analise_combinatoria_arranjo_simples import insert_arrangement


###############################################################  CONJUNTOS NUMERICOS - NUM NATURAIS


# Importar a função do arquivo conjuntos_naturais1.py
from .conjuntos_naturais1 import insert_natural_number


# Importar a função do arquivo conjuntos_naturais2.py
from .conjuntos_naturais2 import insert_no_null_natural_number


# Importar a função do arquivo conjuntos_naturais3.py
from .conjuntos_naturais3 import insert_numeros_naturais_pares


# Importar a função do arquivo conjuntos_naturais4.py
from .conjuntos_naturais4 import insert_natural_odd


###############################################################  CONJUNTOS NUMERICOS - NUM INTEIROS Z


# Importar a função do arquivo conjuntos_inteiros1.py
from .conjuntos_inteiros1 import insert_integer_number


# Importar a função do arquivo conjuntos_inteiros2.py
from .conjuntos_inteiros2 import insert_nonzero_integer_number



# Importar a função do arquivo conjuntos_inteiros3.py
from .conjuntos_inteiros3 import insert_nonnegative_integer_number


# Importar a função do arquivo conjuntos_inteiros4.py
from .conjuntos_inteiros4 import insert_nonpositive_integer_number


# Importar a função do arquivo conjuntos_inteiros5.py
from .conjuntos_inteiros5 import insert_positive_nonzero_integer_number


# Importar a função do arquivo conjuntos_inteiros6.py
from .conjuntos_inteiros6 import insert_negative_nonzero_integer_number


###############################################################  CONJUNTOS NUMERICOS - NUM RACIONAIS


# Importar a função do arquivo conjuntos_racionais1.py
from .conjuntos_racionais1 import insert_rational_number


# Importar a função do arquivo conjuntos_racionais2.py
from .conjuntos_racionais2 import insert_nonzero_rational_number


###############################################################  CONJUNTOS NUMERICOS - NUM IRRACIONAIS, REAIS E COMPLEXOS


# Importar a função do arquivo conjuntos_irracionais.py
from .conjuntos_irracionais import insert_irrational_number


# Importar a função do arquivo conjuntos_reais_e_complexos.py
from .conjuntos_reais_e_complexos import insert_real

# Importar a função do arquivo conjuntos_propriedades.py
from .conjuntos_propriedades import insert_properties_of_number_sets


############################################## DIVISIBILIDADE POR 3, 4, 6, 7, 8, 9


# Importar a função do arquivo divisibilidade_3.py
from .divisibilidade_3 import insert_div_3


########### num 4 - digitar ###################


# Importar a função do arquivo divisibilidade_4_digitar.py
#from .divisibilidade_4_digitar import insert_div_4_digitar



# Importar a função do arquivo divisibilidade_4.py
from .divisibilidade_4 import insert_div_4


# Importar a função do arquivo divisibilidade_6.py
from .divisibilidade_6 import insert_div_6


# Importar a função do arquivo divisibilidade_7.py
from .divisibilidade_7 import insert_div_7


# Importar a função do arquivo divisibilidade_8.py
from .divisibilidade_8 import insert_div_8


# Importar a função do arquivo divisibilidade_9.py
from .divisibilidade_9 import insert_div_9


###############################################################  DIZIMA PERIODICA


# Importar a função do arquivo dizima_periodica.py
from .dizima_periodica import insert_repeating_decimal

############################################################### FATORAÇAO

# Importar a função do arquivo fatoracao.py
from .fatoracao import insert_prime_factorization


############################################################### FATORAÇAO DIGITAR


# Importar a função do arquivo fatoracao_digitar.py
from .fatoracao_digitar import insert_prime_factorization_card



###################################################################  INTERVALOS ABERTOS E FECHADOS


# Importar a função do arquivo intervalos_abertos.py
from .intervalos_abertos import insert_numeric_interval_aberto


# Importar a função do arquivo intervalos_fechados.py
from .intervalos_fechados import insert_numeric_interval_fechado


################### JUROS SIMPLES E COMPOSTOS ################


#JUROS SIMPLES
# Importar a função do arquivo juros_simples .py
from .juros_simples import insert_simple_interest
#from .juros_simples import *


#JUROS COMPOSTOS
# Importar a função do arquivojuros_compostos.py
from .juros_compostos import insert_compound_interest



############################################################### MEDIA ARITMETICA SIMPLES E PONDERADA


# Importar a função do arquivo media_aritmetica_simples.py
from .media_aritmetica_simples import insert_media_aritmetica_simples


# Importar a função do arquivo media_aritmetica_ponderada.py
from .media_aritmetica_ponderada import insert_media_aritmetica_ponderada


###############################################################  MMC e MDC


# Importar a função do arquivo mmc0.py
#from .mmc0 import insert_mmc0


# Importar a função do arquivo mmc1.py
from .mmc1 import insert_mmc1



# Importar a função do arquivo mdc.py
from .mdc import insert_mdc


############################################################### NUM PRIMOS


# Importar a função do arquivo numeros_primos1.py
from .numeros_primos1 import insert_prime_number


# Importar a função do arquivo numeros_primos2.py
from .numeros_primos2 import insert_prime_check



##################### PRODUTOS NOTAVEIS ##########################


# Importar a função do arquivo quadrado_soma.py
from .prodnotaveis_quadrado_soma import insert_quadrado_soma

# Importar a função do arquivo quadrado_diferenca.py
from .prodnotaveis_quadrado_diferenca import insert_quadrado_diferenca

# Importar a função do arquivo produto_soma_diferenca.py
from .prodnotaveis_produto_soma_diferenca import insert_produto_soma_diferenca

# Importar a função do arquivo cubo_soma.py
from .prodnotaveis_cubo_soma import insert_cubo_soma

# Importar a função do arquivo cubo_diferenca.py
from .prodnotaveis_cubo_diferenca import insert_cubo_diferenca




################# REGRA DE 3 SIMPLES ##########################


# Importar a função do arquivo regra_de_3_simples_massa.py
from .regra_de_3_simples_massa import insert_rule_of_three_simple


# Importar a função do arquivo regra_de_3_simples_distancia.py
from .regra_de_3_simples_distancia import insert_rule_of_three_simple_time



############################################################### REGRA DE 3 COMPOSTA


# Importar a função do arquivo regra_de_3_composta.py
from .regra_de_3_composta import insert_regra_composta


############################################################# SISTEMA DE NUMERAÇAO - CLASSE E REPRESENTAÇAO


# Importar a função do arquivo sistemas_de_numeracao_classe.py
from .sistemas_de_numeracao_classe import insert_sistemas_numeracao2


# Importar a função do arquivo sistemas_de_numeracao_representacao.py
from .sistemas_de_numeracao_representacao_numerica import insert_sistemas_numeracao



###################################################################  POTENCIAÇAO






# Importar a função do arquivo potenciacao.py
from .potenciacao import insert_produto_potenciacao


# Importar a função do arquivo potenciacao_fracao.py
from .potenciacao_fracao import insert_produto_potenciacao_fracao



################################################################################################################################################################################################# MENU MATEMATICA


def setup_math_buttons(buttons, editor):
    math_menu = QMenu("Matemática")
    math_menu.setStyleSheet("QMenu { font-size: 16px; border: 2px solid black; background-color: yellow; color: black; }"
                            "QMenu::item:selected { background-color: blue; color: white; color: black; }"
                            "QMenu::separator { height: 2px; background: grey; }"
                            "QMenu::item { padding: 5px; border-bottom: 1px solid black; font-weight: bold; }")




################################################################### BOTAO MATH CAIXA DE DIALOGO

        

    action_math = QAction("Math", math_menu)
    action_math.triggered.connect(lambda _, editor=editor: show_math_dialog(editor))
    math_menu.addAction(action_math)


############################################################### ALGORITMO DA DIVISAO

    
    action_algoritmodiv = QAction("Algoritmo da Divisão (Ctrl+Alt+T)", math_menu)
    action_algoritmodiv.triggered.connect(lambda _, editor=editor: insert_divisao_algoritmo(editor))
    math_menu.addAction(action_algoritmodiv)
    

############################################################### ANALISE COMB


    # Create the "Análise Combinatória" submenu
    combinatory_menu = QMenu("Análise Combinatória", math_menu)

    action_arrangement = QAction("Arranjo Simples (Ctrl+Alt+N)", math_menu)
    action_arrangement.triggered.connect(lambda _, editor=editor: insert_arrangement(editor))
    combinatory_menu.addAction(action_arrangement)
    
    action_permutation_simple = QAction("Permutação Simples", math_menu)
    action_permutation_simple.triggered.connect(lambda _, editor=editor: insert_permutation_simple(editor))
    combinatory_menu.addAction(action_permutation_simple)
    
    # Add the "Análise Combinatória" submenu to the "Matemática" menu
    math_menu.addMenu(combinatory_menu)


################################################################### CONJUNTOS NUM - NUM NATURAIS


    # Create the "Conjuntos Numéricos" submenu
    conjuntosnum_menu = QMenu("Conjuntos Numéricos", math_menu)

    action_numnat = QAction("Números Naturais N", math_menu)
    action_numnat.triggered.connect(lambda _, editor=editor: insert_natural_number(editor))
    conjuntosnum_menu.addAction(action_numnat)


    action_numnat2 = QAction("Números Naturais N* Nao Nulos", math_menu)
    action_numnat2.triggered.connect(lambda _, editor=editor: insert_no_null_natural_number(editor))
    conjuntosnum_menu.addAction(action_numnat2)


    action_numnat3 = QAction("Números Naturais N Pares", math_menu)
    action_numnat3.triggered.connect(lambda _, editor=editor: insert_numeros_naturais_pares(editor))
    conjuntosnum_menu.addAction(action_numnat3)

    action_numnat4 = QAction("Números Naturais N Impares", math_menu)
    action_numnat4.triggered.connect(lambda _, editor=editor: insert_natural_odd(editor))
    conjuntosnum_menu.addAction(action_numnat4)


################################################################# CONJUNTOS NUM - NUMEROS INTEIROS


    action_inteiros = QAction("Números Inteiros Z", math_menu)
    action_inteiros.triggered.connect(lambda _, editor=editor: insert_integer_number(editor))
    conjuntosnum_menu.addAction(action_inteiros)

    action_inteiros2 = QAction("Números Inteiros Z* Nao Nulos", math_menu)
    action_inteiros2.triggered.connect(lambda _, editor=editor: insert_nonzero_integer_number(editor))
    conjuntosnum_menu.addAction(action_inteiros2)

    action_inteiros3 = QAction("Números Inteiros Z+ Nao Negativos", math_menu)
    action_inteiros3.triggered.connect(lambda _, editor=editor: insert_nonnegative_integer_number(editor))
    conjuntosnum_menu.addAction(action_inteiros3)

    action_inteiros4 = QAction("Números Inteiros Z- Nao Positivos", math_menu)
    action_inteiros4.triggered.connect(lambda _, editor=editor: insert_nonpositive_integer_number(editor))
    conjuntosnum_menu.addAction(action_inteiros4)

    action_inteiros5 = QAction("Números Inteiros Z*+ Positivos e sem Zero", math_menu)
    action_inteiros5.triggered.connect(lambda _, editor=editor: insert_positive_nonzero_integer_number(editor))
    conjuntosnum_menu.addAction(action_inteiros5)

    action_inteiros6 = QAction("Números Inteiros Z*- Negativos e sem Zero", math_menu)
    action_inteiros6.triggered.connect(lambda _, editor=editor: insert_negative_nonzero_integer_number(editor))
    conjuntosnum_menu.addAction(action_inteiros6)


################################################################### CONJUNTOS NUM - NUMEROS RACIONAIS


    action_numrac = QAction("Números Racionais Q", math_menu)
    action_numrac.triggered.connect(lambda _, editor=editor: insert_rational_number(editor))
    conjuntosnum_menu.addAction(action_numrac)

    action_racionais_nao_nulos = QAction("Números Racionais Não Nulos Q*", math_menu)
    action_racionais_nao_nulos.triggered.connect(lambda _, editor=editor: insert_nonzero_rational_number(editor))
    conjuntosnum_menu.addAction(action_racionais_nao_nulos)


################################################################### CONJUNTOS NUM - NUMEROS IRRACIONAIS, REAIS E COMPLEXOS

    action_irracionais = QAction("Números Irracionais I", math_menu)
    action_irracionais.triggered.connect(lambda _, editor=editor: insert_irrational_number(editor))
    conjuntosnum_menu.addAction(action_irracionais)

    action_reais = QAction("Números Reais R ou Complexos C", math_menu)
    action_reais.triggered.connect(lambda _, editor=editor: insert_real(editor))
    conjuntosnum_menu.addAction(action_reais)


    action_conjuntos_propriedades = QAction("Propriedades", math_menu)
    action_conjuntos_propriedades.triggered.connect(lambda _, editor=editor: insert_properties_of_number_sets(editor))
    conjuntosnum_menu.addAction(action_conjuntos_propriedades)




    # Add the "Conjuntos Numericos" submenu to the "Matemática" menu
    math_menu.addMenu(conjuntosnum_menu)


############################################################### DIVISIBILIDADE


    # Create the "Divisibilidade" submenu
    divisibilidade_menu = QMenu("Divisibilidade", math_menu)

    action_div3 = QAction("Divisibilidade por 3", math_menu)
    action_div3.triggered.connect(lambda _, editor=editor: insert_div_3(editor))
    divisibilidade_menu.addAction(action_div3)


    #action_div4_2 = QAction("Divisibilidade por 4 - Digitar", math_menu)
    #action_div4_2.triggered.connect(lambda _, editor=editor: insert_div_4_digitar(editor))
    #divisibilidade_menu.addAction(action_div4_2)


    action_div4 = QAction("Divisibilidade por 4", math_menu)
    action_div4.triggered.connect(lambda _, editor=editor: insert_div_4(editor))
    divisibilidade_menu.addAction(action_div4)


    action_div6 = QAction("Divisibilidade por 6", math_menu)
    action_div6.triggered.connect(lambda _, editor=editor: insert_div_6(editor))
    divisibilidade_menu.addAction(action_div6)

    action_div7 = QAction("Divisibilidade por 7", math_menu)
    action_div7.triggered.connect(lambda _, editor=editor: insert_div_7(editor))
    divisibilidade_menu.addAction(action_div7)

    action_div8 = QAction("Divisibilidade por 8", math_menu)
    action_div8.triggered.connect(lambda _, editor=editor: insert_div_8(editor))
    divisibilidade_menu.addAction(action_div8)

    action_div9 = QAction("Divisibilidade por 9", math_menu)
    action_div9.triggered.connect(lambda _, editor=editor: insert_div_9(editor))
    divisibilidade_menu.addAction(action_div9)

    # Add the "Divisibilidade" submenu to the "Matemática" menu
    math_menu.addMenu(divisibilidade_menu)


################################################################### DIZIMA PERIODICA


    action_dizima = QAction("Dízima Periódica", math_menu)
    action_dizima.triggered.connect(lambda _, editor=editor: insert_repeating_decimal(editor))
    math_menu.addAction(action_dizima)


################################################################### FATORAÇAO


    # Create the "Fatoração Numérica" submenu
    fatnum_menu = QMenu("Fatoraçao Numerica", math_menu)

    action_numprimofat = QAction("Fatoraçao Numerica", math_menu)
    action_numprimofat.triggered.connect(lambda _, editor=editor: insert_prime_factorization(editor))
    fatnum_menu.addAction(action_numprimofat)

    action_numprimofat2 = QAction("Fatoraçao Numerica - Digitar Num", math_menu)
    action_numprimofat2.triggered.connect(lambda _, editor=editor: insert_prime_factorization_card(editor))
    fatnum_menu.addAction(action_numprimofat2)

    # Add the "Fatoraçao Numerica" submenu to the "Matemática" menu
    math_menu.addMenu(fatnum_menu)


################################################################### INTERVALOS NUMERICOS ABERTOS E FECHADOS


    # Create the "Intervalos Númericos" submenu
    intervalosnum_menu = QMenu("Intervalos Númericos", math_menu)

    action_int_num_aberto = QAction("Intervalos Númericos Abertos", math_menu)
    action_int_num_aberto.triggered.connect(lambda _, editor=editor: insert_numeric_interval_aberto(editor))
    intervalosnum_menu.addAction(action_int_num_aberto)


    action_int_num_fechado = QAction("Intervalos Númericos Fechados", math_menu)
    action_int_num_fechado.triggered.connect(lambda _, editor=editor: insert_numeric_interval_fechado(editor))
    intervalosnum_menu.addAction(action_int_num_fechado)


    # Add the "Intervalos Númericos" submenu to the "Matemática" menu
    math_menu.addMenu(intervalosnum_menu)


############################################################### JUROS SIMPLES E COMPOSTOS

    
    action_compound_interest = QAction("Juros Compostos", math_menu)
    action_compound_interest.triggered.connect(lambda _, editor=editor: insert_compound_interest(editor))
    math_menu.addAction(action_compound_interest)

    action_simple_interest = QAction("Juros Simples", math_menu)
    action_simple_interest.triggered.connect(lambda _, editor=editor: insert_simple_interest(editor))
    math_menu.addAction(action_simple_interest)



################################################################### MEDIA ARITMETICA SIMPLES E PONDERADA


    action_media_arit_simples = QAction("Média Aritmética Simples", math_menu)
    action_media_arit_simples.triggered.connect(lambda _, editor=editor: insert_media_aritmetica_simples(editor))
    math_menu.addAction(action_media_arit_simples)



    action_media_arit_ponderada = QAction("Média Aritmética Ponderada", math_menu)
    action_media_arit_ponderada.triggered.connect(lambda _, editor=editor: insert_media_aritmetica_ponderada(editor))
    math_menu.addAction(action_media_arit_ponderada)


################################################################### MMC e MDC


    # Create the "MMC" submenu
    #mmc_menu = QMenu("MMC 1", math_menu)

    #action_mmc = QAction("MMC 1", math_menu)
    #action_mmc.triggered.connect(lambda _, editor=editor: insert_mmc0(editor))
    #math_menu.addAction(action_mmc)


    action_mmc2 = QAction("MMC", math_menu)
    action_mmc2.triggered.connect(lambda _, editor=editor: insert_mmc1(editor))
    math_menu.addAction(action_mmc2)

    # Add the "MMC" submenu to the "Matemática" menu
    #math_menu.addMenu(mmc_menu)




    action_mdc = QAction("MDC", math_menu)
    action_mdc.triggered.connect(lambda _, editor=editor: insert_mdc(editor))
    math_menu.addAction(action_mdc)


################################################################### NUMEROS PRIMOS


    # Create the "Números Primos" submenu
    numerosprimos_menu = QMenu("Numeros Primos", math_menu)

    action_numprimo = QAction("Numeros Primos 1", math_menu)
    action_numprimo.triggered.connect(lambda _, editor=editor: insert_prime_number(editor))
    numerosprimos_menu.addAction(action_numprimo)


    action_numprimo2 = QAction("Numeros Primos 2", math_menu)
    action_numprimo2.triggered.connect(lambda _, editor=editor: insert_prime_check(editor))
    numerosprimos_menu.addAction(action_numprimo2)

    # Add the "Numeros Primos" submenu to the "Matemática" menu
    math_menu.addMenu(numerosprimos_menu)


##################### PRODUTOS NOTAVEIS ##########################

    # Create the "Produtos Notáveis" submenu
    prodnot_menu = QMenu("Produtos Notaveis", math_menu)

    action_pncubodif = QAction("Cubo da Diferença", math_menu)
    action_pncubodif.triggered.connect(lambda _, editor=editor: insert_cubo_diferenca(editor))
    prodnot_menu.addAction(action_pncubodif)

    action_pncubosoma = QAction("Cubo da Soma", math_menu)
    action_pncubosoma.triggered.connect(lambda _, editor=editor: insert_cubo_soma(editor))
    prodnot_menu.addAction(action_pncubosoma)

    action_pnsomadif = QAction("Produto da Soma pela Diferença", math_menu)
    action_pnsomadif.triggered.connect(lambda _, editor=editor: insert_produto_soma_diferenca(editor))
    prodnot_menu.addAction(action_pnsomadif)

    action_pnquadradodif = QAction("Quadrado da Diferença", math_menu)
    action_pnquadradodif.triggered.connect(lambda _, editor=editor: insert_quadrado_diferenca(editor))
    prodnot_menu.addAction(action_pnquadradodif)

    action_pnquadradosoma = QAction("Quadrado da Soma", math_menu)
    action_pnquadradosoma.triggered.connect(lambda _, editor=editor: insert_quadrado_soma(editor))
    prodnot_menu.addAction(action_pnquadradosoma)

    # Add the "Produtos Notaveis" submenu to the "Matemática" menu
    math_menu.addMenu(prodnot_menu)


################################################################### REGRA DE 3 SIMPLES


    # Create the "Regra de 3 Simples" submenu
    regrade3simples_menu = QMenu("Regra de 3 Simples", math_menu)

    action_rule_of_three_simple_time = QAction("Regra de 3 Simples (Distancia ou Tempo)", math_menu)
    action_rule_of_three_simple_time.triggered.connect(lambda _, editor=editor: insert_rule_of_three_simple_time(editor))
    regrade3simples_menu.addAction(action_rule_of_three_simple_time)

    action_rule_of_three_simple = QAction("Regra de 3 Simples (Massa ou Peso)", math_menu)
    action_rule_of_three_simple.triggered.connect(lambda _, editor=editor: insert_rule_of_three_simple(editor))
    regrade3simples_menu.addAction(action_rule_of_three_simple)


    # Add the "Regra de 3 simples" submenu to the "Matemática" menu
    math_menu.addMenu(regrade3simples_menu)


################################################################### REGRA DE 3 COMPOSTA


    action_composta = QAction("Regra de 3 Composta", math_menu)
    action_composta.triggered.connect(lambda _, editor=editor: insert_regra_composta(editor))
    math_menu.addAction(action_composta)


################################################################### SISTEMAS NUMERAÇAO


    # Create the "Sistemas de Numeração" submenu
    sistnum_menu = QMenu("Sistemas de Numeraçao", math_menu)

    action_sistema_num2 = QAction("Classe", math_menu)
    action_sistema_num2.triggered.connect(lambda _, editor=editor: insert_sistemas_numeracao2(editor))
    sistnum_menu.addAction(action_sistema_num2)

    action_sistema_num = QAction("Representaçao", math_menu)
    action_sistema_num.triggered.connect(lambda _, editor=editor: insert_sistemas_numeracao(editor))
    sistnum_menu.addAction(action_sistema_num)

    # Add the "Sistemas de Numeraçao" submenu to the "Matemática" menu
    math_menu.addMenu(sistnum_menu)



################################################################### POTENCIAÇAO



    action_potenciacao = QAction("Potenciação", math_menu)
    action_potenciacao.triggered.connect(lambda _, editor=editor: insert_produto_potenciacao(editor))
    math_menu.addAction(action_potenciacao)

    action_potenciacao_fracao = QAction("Potenciação - Fração", math_menu)
    action_potenciacao_fracao.triggered.connect(lambda _, editor=editor: insert_produto_potenciacao_fracao(editor))
    math_menu.addAction(action_potenciacao_fracao)



################################################################### 

   
   

    math_button = editor.addButton(
        icon=None,
        cmd="math-menu",
        #func=lambda editor=editor: math_menu.exec(QCursor.pos()),    ##submenu
        func=lambda editor=editor: show_math_dialog(editor),
        tip="Operações Matemáticas",
        #label="<b>Matemática</b>",

        label=create_button_label1("Matematica", "yellow", "black", "bold"),
        keys="Ctrl+M"
    )
    buttons.append(math_button)
    return buttons


def create_button_label1(text: str, background_color: str, text_color: str, font_weight: str) -> str:
    return f"<span style='background-color:{background_color};color:{text_color};font-weight:{font_weight};'>{text}</span>"





#gui_hooks.editor_did_init_buttons.append(setup_math_buttons)


def show_math_dialog(editor):
    global dialog  # Mantém uma referência global à caixa de diálogo
    dialog = CustomDialogs(editor)
    dialog.show()


####################

from .botao_matematica import *

gui_hooks.editor_did_init_buttons.append(setup_math_buttons)


####################################################################################################################################################################################################################### BOTAO BANDEIRA DO BRASIL


# Importar a função do arquivo imagem.py
#from .imagem import ImageManager, ImageDialog  # Importar as classes do arquivo imagem.py
from .imagem import *


from .botao_formula import *



