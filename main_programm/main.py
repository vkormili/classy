import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton
import csv
import re


def get_list_items(filename: str) -> list:
    f = open(filename, 'r')
    reader = csv.reader(f, delimiter=';')
    lst = []
    for row in reader:
        lst.append(row[0])
    f.close()
    return lst


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

        self.lineEdit.textEdited.connect(self.searching)

    def check(self):
        user_guess = self.sender().text()
        self.textBrowser.insertPlainText('\n' + user_guess + '\n')

    def back(self):
        ex.show()
        self.close()

    def searching(self):
        while self.search.count():
            widget = self.search.takeAt(0).widget()
            self.search.removeWidget(widget)
        to_find = self.lineEdit.text()
        all_items = get_list_items('probe.csv')
        results = []
        for item in all_items:
            try:
                results.append(re.fullmatch(f'.*{to_find}.*', item)[0])
            except TypeError:
                pass
        for result in results[:8]:
            btn_search = QPushButton(result)
            btn_search.clicked.connect(self.check)
            self.search.addWidget(btn_search)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartPage()
    ex.show()
    sys.exit(app.exec_())
