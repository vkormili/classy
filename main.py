import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTextEdit, QLabel
from PyQt5.QtCore import Qt


class StartPage(QMainWindow):
    # инициализация стартовой страницы
    def __init__(self):
        super().__init__()
        uic.loadUi('start_page.ui', self)
        # ставим заголовок
        self.setWindowTitle('Classy')
        # подключаем кнопки
        self.anim_btn.clicked.connect(self.start)
        self.plant_btn.clicked.connect(self.start)
        self.lang_btn.clicked.connect(self.start)

    def start(self):
        # при нажатии на кнопку создаётся новое окно и передаётся выбранный режим
        if self.sender().text() == 'Животные':
            self.second_form = Game(self, 'anim')
        elif self.sender().text() == 'Растения':
            self.second_form = Game(self, 'plant')
        elif self.sender().text() == 'Языки':
            self.second_form = Game(self, 'lang')
        self.second_form.show()
        ex.close()


class Game(QWidget):
    # инициализация игрового интерфейса
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('game_interface.ui', self)
        self.setWindowTitle('Classy')
        self.mode = args[1]
        # в зависимости от режима наполняем интерфейс
        if self.mode == 'anim':
            self.lineEdit.insert('животного')
            # создаем название уровней генеалогии
            type_label = QLabel('тип')
            class_label = QLabel('класс')
            otrad_label = QLabel('отряд')
            family_label = QLabel('семья')
            rod_label = QLabel('род')
            vid_label = QLabel('вид')
            self.progressBar.setMaximum(6)
            # добавляем на экран
            self.levels.addWidget(type_label)
            self.levels.addWidget(class_label)
            self.levels.addWidget(otrad_label)
            self.levels.addWidget(family_label)
            self.levels.addWidget(rod_label)
            self.levels.addWidget(vid_label)
        elif self.mode == 'plant':
            self.lineEdit.insert('растения')
            # создаем название уровней генеалогии
            type_label = QLabel('тип')
            class_label = QLabel('класс')
            otrad_label = QLabel('отряд')
            family_label = QLabel('семья')
            rod_label = QLabel('род')
            vid_label = QLabel('вид')
            self.progressBar.setMaximum(6)
            # добавляем на экран
            self.levels.addWidget(type_label)
            self.levels.addWidget(class_label)
            self.levels.addWidget(otrad_label)
            self.levels.addWidget(family_label)
            self.levels.addWidget(rod_label)
            self.levels.addWidget(vid_label)
        elif self.mode == 'lang':
            self.lineEdit.insert('языка')

        self.back_btn.clicked.connect(self.back)

        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)

        self.guess_list = QTextEdit()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            user_guess = self.lineEdit.text()

    def back(self):
        ex.show()
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartPage()
    ex.show()
    sys.exit(app.exec_())