import random
import os
import json
import math
import datetime
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QTimer

from aqt.editor import Editor
from aqt import gui_hooks, mw



from PyQt6.QtGui import QColor


#################################



# Caminho para o arquivo formulas.txt dentro da pasta do addon
addon_path = os.path.dirname(__file__)
txt_file = os.path.join(addon_path, "formulas.txt")
#last_training_file = os.path.join(addon_path, "last_training.json")

class CustomDialog(QDialog):
    def __init__(self, editor):
        super().__init__(None, Qt.WindowType.Window | Qt.WindowType.WindowMinimizeButtonHint | Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowStaysOnTopHint)
        self.editor = editor
        self.setWindowTitle("👨‍🔬 FORMULAS 👨‍🔬")
        self.setModal(False)
        self.setStyleSheet("""
            background-color: #E0F7FA;
            font-size: 22px;
            color: black;
        """)
        self.setGeometry(100, 100, 1000, 600)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)



        self.list_widget = QListWidget()
        self.load_text()

        layout.addWidget(self.list_widget)

        button_layout = QHBoxLayout()

        def add_text():
            #global ok
            dialog = QInputDialog(self)
            dialog.setFixedSize(600, 400)
            dialog.setWindowTitle('Adicionar')
            dialog.setLabelText('Digite o texto:')

            dialog.setWindowModality(Qt.WindowModality.NonModal)  # Permitir interação com outras janelas
            dialog.show()


            ok = dialog.exec()
            if ok:
                new_text = dialog.textValue().strip()
                if new_text:
                    # Conta quantos itens já existem na lista
                    count = self.list_widget.count()
                    # Adiciona o novo item com o número correto
                    item_text = f"{count + 1}. {new_text}"
                    item = QListWidgetItem(item_text)
                    if "Exemplo" in item_text:
                        item.setForeground(Qt.GlobalColor.red)
                    if "Treinar" in item_text:
                        item.setForeground(Qt.GlobalColor.blue)
                    self.list_widget.addItem(item)

        def edit_text():
            selected_item = self.list_widget.currentItem()
            if selected_item:
                current_text = selected_item.text()
                dialog = QInputDialog(self)
                dialog.setFixedSize(600, 400)
                dialog.setWindowTitle('Editar')
                dialog.setLabelText('Edite o texto:')
                dialog.setTextValue(current_text.split('.', 1)[1].strip())

                dialog.setWindowModality(Qt.WindowModality.NonModal)  # Permitir interação com outras janelas
                dialog.show()

                ok = dialog.exec()
                if ok:
                    edited_text = dialog.textValue().strip()
                    if edited_text:
                        item_text = f"{self.list_widget.row(selected_item) + 1}. {edited_text}"
                        selected_item.setText(item_text)
                        if "Exemplo" in item_text:
                            selected_item.setForeground(Qt.GlobalColor.red)
                        elif "Treinar" in item_text:
                            selected_item.setForeground(Qt.GlobalColor.blue)
                        else:
                            selected_item.setForeground(Qt.GlobalColor.black)

        def remove_text():
            selected_item = self.list_widget.currentItem()
            if selected_item:
                row = self.list_widget.row(selected_item)
                self.list_widget.takeItem(row)
                # Atualiza os números após remover um item
                self.update_numbers()

        def save_text():
            with open(txt_file, 'w', encoding='utf-8') as file:
                for index in range(self.list_widget.count()):
                    item = self.list_widget.item(index)
                    file.write(item.text().split('.', 1)[1].strip() + '\n')

        def sort_text():
            items = []
            for index in range(self.list_widget.count()):
                # Obtém o texto completo do item
                item_text = self.list_widget.item(index).text()
                # Remove o número no início e adiciona na lista
                items.append(item_text.split('.', 1)[1].strip())

            # Ordena os itens pelo texto (ignorando o número)
            items.sort(key=str.lower)

            self.list_widget.clear()
            for index, line in enumerate(items, start=1):
                # Adiciona o item com o número correto
                item_text = f"{index}. {line}"
                item = QListWidgetItem(item_text)
                if "Exemplo" in item_text:
                    item.setForeground(Qt.GlobalColor.red)
                if "Treinar" in item_text:
                    item.setForeground(Qt.GlobalColor.blue)
                self.list_widget.addItem(item)

            # Salva a lista ordenada no arquivo
            with open(txt_file, 'w', encoding='utf-8') as file:
                for line in items:
                    file.write(line + '\n')

        add_button = QPushButton('Adicionar')
        add_button.setStyleSheet("""
            background-color: #8BC34A;
            font-size: 16px;
            color: black;
        """)
        add_button.clicked.connect(add_text)
        button_layout.addWidget(add_button)

        edit_button = QPushButton('Editar')
        edit_button.setStyleSheet("""
            background-color: #8BC34A;
            font-size: 16px;
            color: black;
        """)
        edit_button.clicked.connect(edit_text)
        button_layout.addWidget(edit_button)

        remove_button = QPushButton('Remover')
        remove_button.setStyleSheet("""
            background-color: #8BC34A;
            font-size: 16px;
            color: black;
        """)
        remove_button.clicked.connect(remove_text)
        button_layout.addWidget(remove_button)

        sort_button = QPushButton('Ordenar')
        sort_button.setStyleSheet("""
            background-color: #8BC34A;
            font-size: 16px;
            color: black;
        """)
        sort_button.clicked.connect(sort_text)
        button_layout.addWidget(sort_button)

        save_button = QPushButton('Salvar')
        save_button.setStyleSheet("""
            background-color: #8BC34A;
            font-size: 16px;
            color: black;
        """)
        save_button.clicked.connect(save_text)
        button_layout.addWidget(save_button)

        layout.addLayout(button_layout)
        layout.addWidget(self.list_widget)




        # Caixa de pesquisa e botão de pesquisa
        search_layout = QHBoxLayout()
        self.search_text = QLineEdit()
        self.search_text.setStyleSheet("""
        background-color: #FFFFFF; /* fundo branco */
        border: 1px solid #000000; /* borda preta */
        font-size: 22px;
        color: black;
        """)
        self.search_text.setPlaceholderText("Digite aqui")  # Define o texto do placeholder, fundo de texto transparente na caixa de texto

        search_layout.addWidget(self.search_text)
        search_button = QPushButton('Pesquisar')
        search_button.setStyleSheet("""
            background-color: #8BC34A;
            font-size: 22px;            
            color: black;
            
        """)
        search_button.clicked.connect(self.search_text_in_list)
        search_layout.addWidget(search_button)

        layout.addLayout(search_layout)




        self.list_widget.itemClicked.connect(self.example_or_train)

    def load_text(self):
        with open(txt_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            self.list_widget.clear()
            for index, line in enumerate(lines, start=1):
                item_text = f"{index}. {line.strip()}"
                item = QListWidgetItem(item_text)
                if "Exemplo" in item_text:
                    item.setForeground(Qt.GlobalColor.red)
                if "Treinar" in item_text:
                    item.setForeground(Qt.GlobalColor.blue)
                self.list_widget.addItem(item)



    def search_text_in_list(self):
        # Limpar destaque amarelo da pesquisa anterior
        for index in range(self.list_widget.count()):
            item = self.list_widget.item(index)
            item.setBackground(QColor(Qt.GlobalColor.white))  # Voltar cor de fundo para branco

        search_term = self.search_text.text().strip()
        if not search_term:
            QMessageBox.warning(self, "Aviso", "Precisa digitar um texto para pesquisar.")
            return

        found = False
        for index in range(self.list_widget.count()):
            item = self.list_widget.item(index)
            if search_term.lower() in item.text().lower():
                item.setBackground(QColor(Qt.GlobalColor.yellow))  # Definir cor de fundo como amarelo
                self.list_widget.scrollToItem(item)
                found = True

        if not found:
            QMessageBox.information(self, "Informação", f"A palavra '{search_term}' não existe no texto.")





#######################################################




    def example_or_train(self, item):
         selected_line = item.text()
         if "Analise Combinatoria -> Arranjo Simples: Exemplo" in selected_line:
             self.show_exemplo_arranjo_simples()

         elif "Analise Combinatoria -> Arranjo Simples: Treinar" in selected_line:
             self.treino_arranjo_simples()

         elif "Analise Combinatoria -> Permutaçao Simples: Treinar" in selected_line:
             self.treino_permutacao_simples()

         elif "Analise Combinatoria -> Permutaçao Simples: Exemplo" in selected_line:
             self.show_exemplo_permutacao_simples()
         else:
             self.insert_random_line(selected_line)







    def insert_random_line(self, line):
        current_note = self.editor.note
        current_field = self.editor.currentField
        
        if current_field is None:
            #QMessageBox.warning(self, "Aviso", "Nenhum campo está selecionado.")
            #return
            current_field = 0
    


        self.editor.web.eval("focusField(%d);" % current_field)
        current_text = current_note.fields[current_field]

        if current_text.endswith('<br>'):
            current_note.fields[current_field] += f"{line}<br>"
        else:
            current_note.fields[current_field] += f"{line}<br>"

        self.editor.loadNote()


########################## EXEMPLOS aqui é gambiarra pura, espero que ninguem note esses nbsp kkkk by Eros


#    def show_formula_arranjosimples(self):
#        n = random.randint(3, 10)
#        p = random.randint(1, n-1)

#        example_text = (
#            f"<span style='color: red;'>Analise Combinatoria -> Arranjo Simples</span><br>"
#            f"Quantos arranjos existem de {n} elementos tomados de {p} em {p}?<br><br>"

            #f"An,k = \\(\\frac{{{n}!}}{{({n}-{p})!}}\\)<br><br>"    #mathjax nao funciona aqui

#            f"An,k = n!<br>"
#            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_____<br>"
#            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(n-k)!<br><br>"
#            f"An,k = {n}!<br>"
#            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_____<br>"
#            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;({n}-{p})!<br><br>"
#            f"An,k = {n}!<br>"
#            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_____<br>"
#            f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{n-p}!<br><br>"
#            f"An,k = {n} x {' x '.join(str(i) for i in range(n-1, n-p, -1))} = {self.calculate_arrangement(n, p)}"
#        )

#        QMessageBox.information(self, "Exemplo de Arranjo Simples", example_text)

#    def calculate_arrangement(self, n, p):
#        result = 1
#        for i in range(n, n-p, -1):
#            result *= i
#        return result

    












#    def show_formula_permutacaosimples(self):
#        n = self.generate_random_number()
#        numbers = list(range(n, 0, -1))

#        example_text = (
#            f"<span style='color: red;'>Analise Combinatoria -> Permutação Simples</span><br>"
#            f"Quantas permutações existem de {n} elementos?<br><br>"

#            f"Pn = n!<br>"
#            f"Pn = {n}!<br>"
#            f"Pn = {' x '.join(str(i) for i in numbers)}<br>"
#            f"Pn = {self.calculate_permutation(n)}"
#        )

#        QMessageBox.information(self, "Exemplo de Permutação Simples", example_text)


#    def calculate_permutation(self, n):
#        result = 1
#        for i in range(n, 0, -1):
#            result *= i
#        return result

#    def generate_random_number(self):
#        n = random.randint(3, 10)
#        return n





########################## 


    def update_numbers(self):
        for index in range(self.list_widget.count()):
            item = self.list_widget.item(index)
            text = item.text().split('.', 1)[1].strip()
            item.setText(f"{index + 1}. {text}")
            if "Exemplo" in item.text():
                item.setForeground(Qt.GlobalColor.red)
            elif "Treinar" in item.text():
                item.setForeground(Qt.GlobalColor.blue)
            else:
                item.setForeground(Qt.GlobalColor.black)

    def treino_arranjo_simples(self):
        global training_dialog
        training_dialog = Arranjo_Simples_Treino(self)
        training_dialog.show()

    def treino_permutacao_simples(self):
        global training_dialog
        training_dialog = Permutacao_Simples_Treino(self)
        training_dialog.show()

    def show_exemplo_arranjo_simples(self):
        global example_dialog
        example_dialog = ExemploArranjoSimples(self)
        example_dialog.show()

    def show_exemplo_permutacao_simples(self):
        global example_dialog
        example_dialog = ExemploPermutacaoSimples(self)
        example_dialog.show()


########################################################################################################################################## treinar




from .analise_combinatoria_arranjo_simples_Treino import *
from .analise_combinatoria_permutacao_simples_Treino import *

from .analise_combinatoria_arranjo_simples_Exemplo import *
from .analise_combinatoria_permutacao_simples_Exemplo import *


######################################################################################### 


def add_text_buttons(buttons, editor):
    random_line_button = editor.addButton(
        None,
        'Random Line',
        lambda e=editor: show_dialog(editor),
        tip='Formulas de Matematica',
        label=create_button_label("Formulas", "#8BC34A", "black", "bold"),
    )
    buttons.append(random_line_button)
    return buttons



def show_dialog(editor):
    global dialog
    dialog = CustomDialog(editor)
    dialog.show()


def create_button_label(text: str, background_color: str, text_color: str, font_weight: str) -> str:
    return f"<span style='background-color:{background_color};color:{text_color};font-weight:{font_weight};'>{text}</span>"

gui_hooks.editor_did_init_buttons.append(add_text_buttons)

