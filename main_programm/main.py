import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton
import csv
import re
import functions


def get_list_items(filename: str) -> list:
    # получает список всех единиц из csv файла
    f = open(filename, 'r', newline='', encoding='utf-8')
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
        self.answer = functions.asking(self.mode)

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

            self.guess_status.setText(self.guess_status.text() + ' царство')

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

            self.guess_status.setText(self.guess_status.text() + ' царство')

        elif self.mode == 'lang':
            self.lineEdit.insert('языка')
            self.progressBar.setMaximum(0)

        # подключение действия для кнопки на главную страницу
        self.back_btn.clicked.connect(self.back)

        # устанавливаем значения для шкалы прогресса
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        # подключаем поисковую строку
        self.lineEdit.textEdited.connect(self.searching)

    def check(self):
        # действие проверки ответа от пользователя
        user_guess = self.sender().text()
        self.textBrowser.insertPlainText(user_guess + '\n')
        # сверяем ответ с правильным
        ball, level = functions.proxi(self.answer, user_guess, self.mode)
        if self.progressBar.value() < ball:
            # если продвинулся, то отображаем на экране
            self.guess_status.setText('Угадан уровень генеалогии: ' + level)
            self.progressBar.setValue(ball)
            # если угадал
            if self.progressBar.value() == self.progressBar.maximum():
                self.guess_status.setText('ура! ты победил(а)!')


    def back(self):
        # возвращение на главную
        ex.show()
        self.close()

    def searching(self):
        # функционал поисковой строки
        # очистка предыдущих запросов
        while self.search.count():
            widget = self.search.takeAt(0).widget()
            self.search.removeWidget(widget)
        # поиск регулярными выражениями по запросу
        to_find = self.lineEdit.text()
        all_items = get_list_items('animals.csv')
        results = []
        for item in all_items:
            try:
                results.append(re.fullmatch(f'.*{to_find}.*', item)[0])
            except TypeError:
                pass
        # вывод некоторых результатов на экран
        for result in results[:15]:
            btn_search = QPushButton(result)
            btn_search.clicked.connect(self.check)
            self.search.addWidget(btn_search)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartPage()
    ex.show()
    sys.exit(app.exec_())
