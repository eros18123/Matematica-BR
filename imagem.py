import random
import os
import json
import math
from random import randint, sample
from math import factorial
from aqt.qt import *
from aqt.editor import Editor
from itertools import permutations

from aqt import mw
from anki.hooks import addHook
from anki.notes import Note

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QFileDialog, QTextBrowser, QScrollArea, QWidget
from PyQt6.QtGui import QPixmap, QFont, QIcon
from PyQt6.QtCore import Qt
from aqt import gui_hooks, mw

ADDON_NAME = os.path.basename(__file__).replace(".py", "")

class ImageManager:
    def __init__(self, editor):
        self.editor = editor
        self.img_button = None
        self.label_flag = None
        self.flag_icon_path = self.load_icon_path()

    def load_icon_path(self):
        addon_data_folder = mw.pm.addonFolder()
        config_path = os.path.join(addon_data_folder, "config.json")

        if os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f)
                icon_path = config.get("icon_path", None)
                if icon_path and os.path.exists(icon_path):
                    return icon_path
                else:
                    return os.path.join(os.path.dirname(__file__), 'br.jpg')
        else:
            return os.path.join(os.path.dirname(__file__), 'br.jpg')

    def save_icon_path(self, icon_path):
        addon_data_folder = mw.pm.addonFolder()
        config_path = os.path.join(addon_data_folder, "config.json")

        config = {"icon_path": icon_path}
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=4)

    def setup_img_button(self, buttons):
        self.img_button = self.create_button(self.flag_icon_path)
        buttons.append(self.img_button)
        return buttons

    def create_button(self, icon_path):
        if icon_path and os.path.exists(icon_path):
            img_button = self.editor.addButton(
                icon=icon_path,
                cmd="img-action",
                func=lambda editor=self.editor: self.show_dialog(editor),
                tip="Informaçoes do Autor"
            )
        else:
            img_button = self.editor.addButton(
                icon=None,
                cmd="info-action",
                label="Informações",
                func=lambda editor=self.editor: self.show_dialog(editor),
                tip="Informações do Autor"
            )
        return img_button

    def show_dialog(self, editor):
        global dialog
        dialog = ImageDialog(self, editor)
        dialog.show()

    def change_image(self, file_name):
        try:
            if file_name:
                self.flag_icon_path = file_name
                self.save_icon_path(file_name)
                self.update_image_label(self.label_flag, file_name)
                self.update_button_icon(file_name)
        except Exception as e:
            print(f"Erro ao trocar a imagem: {e}")

    def update_image_label(self, label, icon_path):
        pixmap = QPixmap(icon_path)
        pixmap = pixmap.scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        label.setPixmap(pixmap)
        label.setFixedSize(pixmap.size())

    def update_button_icon(self, icon_path):
        if self.img_button:
            if os.path.exists(icon_path):
                self.img_button.setIcon(QIcon(icon_path))
            else:
                self.img_button.setIcon(QIcon())

class ImageDialog(QDialog):
    def __init__(self, manager, editor):
        super().__init__(editor.parentWindow)
        self.manager = manager
        self.setWindowTitle("Informações do Autor")
        self.resize(450, 600)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        self.content = QWidget()
        self.layout = QVBoxLayout(self.content)
        
        self.setup_ui()
        
        self.scroll_area.setWidget(self.content)
        
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

    def setup_ui(self):
        self.label_flag = QLabel()
        self.manager.update_image_label(self.label_flag, self.manager.flag_icon_path)
        self.layout.addWidget(self.label_flag)

        label_autor = self.create_text_browser("👨‍🔬 Autor: Eros Cardoso")
        label_versao = self.create_text_browser("🔵 Versão: 1.1 - mes/ano 07/24")
        label_whatsapp = self.create_text_browser("🟢 Whatsapp: <a href='https://bit.ly/ankibrasil'>https://bit.ly/ankibrasil</a>", True)
        label_email = self.create_text_browser("💌 E-mail: <a href='mailto:eros18123@gmail.com'>eros18123@gmail.com</a>", True)
        label_yt = self.create_text_browser("🔴 Youtube: <a href='https://www.youtube.com/channel/UC6NyBWP-lmxWWU5-fpevX2g'>@anki_brasil</a>", True)
        label_teleg = self.create_text_browser("🧊Telegram: <a href='https://bit.ly/ankitel'>https://bit.ly/ankitel</a>", True)

        label_consid = self.create_text_browser("📚 Considerações: Addon desenvolvido para ajudar os estudantes de ENEM e Concurso no Brasil <br> Addon em fase de desenvolvimento, novas atualizações podem surgir com o tempo", True, 90)
        label_duvidas = self.create_text_browser("❓ Dúvidas / Bugs / Sugestões: Envie para o e-mail acima ou entre em contato pelas redes sociais", True, 50)
        label_creditos = self.create_text_browser("👍 Créditos: <a href='https://chatgpt.com'>Chatgpt</a>, <a href='https://www.perplexity.ai'>Perplexity</a>, <a href='https://www.todamateria.com.br'>Toda Materia</a> e <a href='https://brasilescola.uol.com.br'>Brasil Escola</a>", True, 50)

        change_img_button = QPushButton("Trocar Imagem")
        change_img_button.clicked.connect(self.change_image_dialog)

        self.layout.addWidget(label_autor)
        self.layout.addWidget(label_versao)
        self.layout.addWidget(label_whatsapp)
        self.layout.addWidget(label_email)
        self.layout.addWidget(label_yt)
        self.layout.addWidget(label_teleg)
        self.layout.addWidget(label_consid)
        self.layout.addWidget(label_duvidas)
        self.layout.addWidget(label_creditos)
        self.layout.addWidget(change_img_button)

        self.adjustSize()

    def create_text_browser(self, text, open_external_links=False, min_height=None):
        text_browser = QTextBrowser()
        text_browser.setHtml(f"<div style='text-align: justify; hyphens: auto;'>{text}</div>")
        text_browser.setFont(QFont("Arial", 12))
        if open_external_links:
            text_browser.setOpenExternalLinks(True)
        if min_height:
            text_browser.setFixedHeight(min_height)
        else:
            text_browser.setFixedHeight(text_browser.document().size().height() + 30)
        return text_browser

    def change_image_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Selecione a nova imagem",
            "",
            "Imagens (*.png *.jpg *.jpeg *.gif);;Todos os Arquivos (*)"
        )

        if file_name:
            self.manager.change_image(file_name)
            self.manager.flag_icon_path = file_name
            self.manager.update_image_label(self.label_flag, file_name)

def initialize_buttons(buttons, editor):
    image_manager = ImageManager(editor)
    return image_manager.setup_img_button(buttons)

gui_hooks.editor_did_init_buttons.append(initialize_buttons)
