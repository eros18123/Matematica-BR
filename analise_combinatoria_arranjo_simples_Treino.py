import os
import random
import datetime
import json
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QRadioButton, QButtonGroup, QPushButton, QApplication, QDialogButtonBox, QHBoxLayout
from PyQt6.QtCore import QTimer, Qt

addon_path = os.path.dirname(__file__)
score_file = os.path.join(addon_path, "scores_arranjo_simples.json")
last_training_file = os.path.join(addon_path, "last_training_arranjo_simples.json")

class FinalScoreDialog(QDialog):
    def __init__(self, correct_answers, incorrect_answers, score, total_correct_answers, total_incorrect_answers, total_score, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Resultado Final")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout(self)
        score_label = QLabel(f"Pontuação do dia - Acertos: {correct_answers}, Erros: {incorrect_answers}, Total de pontos: {score}", self)
        layout.addWidget(score_label)
        total_score_label = QLabel(f"Pontuação total - Acertos: {total_correct_answers}, Erros: {total_incorrect_answers}, Total de pontos: {total_score}", self)
        layout.addWidget(total_score_label)
        if correct_answers <= 2:
            message = "Pessimo: Você não está apto nesta matéria, treine mais"
        elif correct_answers <= 5:
            message = "Razoavel: Você ainda não está bem, precisa melhorar. ⭐"
        elif correct_answers <= 8:
            message = "Bom: Você está bem, mas precisa treinar mais se quiser passar em algum concurso. ⭐ ⭐"
        else:
            message = "Excelente: Você está preparado para passar em qualquer concurso nesta matéria, parabéns! ⭐ ⭐ ⭐"
        if correct_answers <= 10:
            message += " ⭐"
        message_label = QLabel(message, self)
        layout.addWidget(message_label)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)

class Arranjo_Simples_Treino(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Treinamento de Arranjo Simples")
        self.setGeometry(100, 100, 600, 400)

        self.questions = self.generate_questions()

        self.current_question = 0
        self.score = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.time_left = 60
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.final_score_shown = False
        self.total_correct_answers = 0
        self.total_incorrect_answers = 0
        self.total_score = 0
        self.previous_score = 0
        self.load_scores()
        self.init_ui()
        self.show_question()

    def can_train_today(self):
        if os.path.exists(last_training_file):
            with open(last_training_file, 'r', encoding='utf-8') as file:
                last_training_date = json.load(file)['date']
            today = datetime.date.today()
            return today.strftime("%Y-%m-%d") != last_training_date
        return True

    def init_ui(self):
        self.layout = QVBoxLayout(self)
        self.question_label = QLabel("", self)
        self.question_label.setStyleSheet("font-weight: bold; font-size: 22px;")
        self.layout.addWidget(self.question_label)
        self.options = QButtonGroup(self)
        self.option_buttons = []
        for i in range(4):
            option_button = QRadioButton("", self)
            option_button.setStyleSheet("font-size: 22px;")
            self.option_buttons.append(option_button)
            self.options.addButton(option_button)
            self.layout.addWidget(option_button)
            option_button.clicked.connect(self.check_answer)
        self.feedback_label = QLabel("", self)
        self.feedback_label.setStyleSheet("font-size: 22px;")
        self.layout.addWidget(self.feedback_label)
        self.score_label = QLabel(f"Pontuação: {self.score}", self)
        self.score_label.setStyleSheet("font-size: 22px;")
        self.layout.addWidget(self.score_label)
        self.timer_label = QLabel(f"Tempo restante: {self.time_left} segundos", self)
        self.timer_label.setStyleSheet("font-size: 22px;")
        self.layout.addWidget(self.timer_label)
        button_layout = QHBoxLayout()
        show_score_button = QPushButton("Mostrar Pontuação Atual")
        show_score_button.setStyleSheet("background-color: yellow; color: black; font-size: 22px;")
        show_score_button.clicked.connect(self.show_current_score)
        button_layout.addWidget(show_score_button)
        self.layout.addLayout(button_layout)


########################################################################


    def generate_questions(self):

        questions = []
        for i in range(1, 11):
            n = random.randint(3, 10)
            p = random.randint(1, n-1)
            correct_answer = 1
            for j in range(n, n-p, -1):
                correct_answer *= j
            wrong_answers = set()
            while len(wrong_answers) < 3:
                wrong_answer = correct_answer + random.randint(-10, 10)
                if wrong_answer != correct_answer and wrong_answer > 0:
                    wrong_answers.add(wrong_answer)
            options = list(wrong_answers) + [correct_answer]
            random.shuffle(options)
            question_text = f"<b>Questão {i}: Quantos arranjos existem de {n} elementos tomados de {p} em {p}?</b>"
            questions.append((question_text, correct_answer, options))
        return questions



########################################################################



    def generate_wrong_answers(self, correct_answer):
        wrong_answers = set()
        while len(wrong_answers) < 3:
            wrong_answer = correct_answer + random.randint(-10, 10)
            if wrong_answer != correct_answer and wrong_answer > 0:
                wrong_answers.add(wrong_answer)
        return list(wrong_answers)

    def show_question(self):
        self.reset_colors()
        if self.current_question < len(self.questions):
            question_text, correct_answer, options = self.questions[self.current_question]
            self.question_label.setText(question_text)
            for btn, option in zip(self.option_buttons, options):
                btn.setText(chr(ord('a') + options.index(option)) + ") " + str(option))
                btn.setChecked(False)
            self.feedback_label.setText("")
            self.time_left = 60
            self.timer_label.setText(f"Tempo restante: {self.time_left} segundos")
            self.timer.start(1000)
        else:
            self.timer.stop()
            self.update_last_training_date()
            self.save_scores()
            self.close()

    def reset_colors(self):
        for btn in self.option_buttons:
            btn.setStyleSheet("color: black; font-size: 22px;")

    def check_answer(self):
        self.timer.stop()
        selected_button = self.options.checkedButton()
        if selected_button:
            selected_answer = int(selected_button.text().split(")")[1].strip())
            if self.current_question < len(self.questions):
                correct_answer = self.questions[self.current_question][1]
                if selected_answer == correct_answer:
                    self.feedback_label.setText("Correto!")
                    self.feedback_label.setStyleSheet("color: green; font-size: 22px;")
                    self.score += 1
                    self.correct_answers += 1
                    self.total_correct_answers += 1
                    selected_button.setStyleSheet("color: green; font-size: 22px;")
                else:
                    self.feedback_label.setText(f"Incorreto! Resposta correta: {correct_answer}")
                    self.feedback_label.setStyleSheet("color: red; font-size: 22px;")
                    self.score -= 1
                    self.incorrect_answers += 1
                    self.total_incorrect_answers += 1
                    selected_button.setStyleSheet("color: red; font-size: 22px;")
                self.total_score += 1 if selected_answer == correct_answer else -1
                self.save_scores()
                self.score_label.setText(f"Pontuação: {self.score}")
                self.current_question += 1
                QTimer.singleShot(2000, self.show_question)

    def time_up(self):
        self.timer.stop()
        if self.current_question < len(self.questions):
            correct_answer = self.questions[self.current_question][1]
            self.feedback_label.setText("Tempo esgotado! Resposta incorreta.")
            self.feedback_label.setStyleSheet("color: red; font-size: 22px;")
            self.score -= 1
            self.incorrect_answers += 1
            self.total_incorrect_answers += 1
            self.total_score -= 1
            self.save_scores()
            self.score_label.setText(f"Pontuação: {self.score}")
            self.current_question += 1
            QTimer.singleShot(2000, self.show_question)

    def update_timer(self):
        self.time_left -= 1
        self.timer_label.setText(f"Tempo restante: {self.time_left} segundos")
        if self.time_left <= 0:
            self.time_up()

    def highlight_correct_answer(self):
        correct_answer = self.questions[self.current_question][1]
        for btn in self.option_buttons:
            if int(btn.text().split(")")[1].strip()) == correct_answer:
                btn.setStyleSheet("color: green; font-size: 22px;")


    def update_last_training_date(self):
        today = datetime.date.today()
        with open(last_training_file, 'w', encoding='utf-8') as file:
            json.dump({'date': today.strftime("%Y-%m-%d")}, file)

    def save_scores(self):
        scores_data = {
            'total_correct_answers': self.total_correct_answers,
            'total_incorrect_answers': self.total_incorrect_answers,
            'total_score': self.total_score,
            'daily_correct_answers': self.correct_answers,
            'daily_incorrect_answers': self.incorrect_answers,
            'daily_score': self.score
        }
        with open(score_file, 'w', encoding='utf-8') as file:
            json.dump(scores_data, file)

    def load_scores(self):
        if os.path.exists(score_file):
            with open(score_file, 'r', encoding='utf-8') as file:
                scores_data = json.load(file)
            self.total_correct_answers = scores_data['total_correct_answers']
            self.total_incorrect_answers = scores_data['total_incorrect_answers']
            self.total_score = scores_data['total_score']
            self.score = scores_data['daily_score']

    def show_current_score(self):

        dialog = FinalScoreDialog(
            self.correct_answers, self.incorrect_answers, self.score,
            self.total_correct_answers, self.total_incorrect_answers, self.total_score, self
        )
        #dialog.exec()

        dialog.setWindowModality(Qt.WindowModality.NonModal)  # Permitir interação com outras janelas
        dialog.show()

