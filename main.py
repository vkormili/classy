import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class StartPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start_page.ui', self)
        self.anim_btn.clicked.connect(self.start)
        self.plant_btn.clicked.connect(self.start)
        self.lang_btn.clicked.connect(self.start)

    def start(self):
        if self.sender().text() == 'Животные':
            self.second_form = Game(self, 'anim')
        elif self.sender().text() == 'Растения':
            self.second_form = Game(self, 'plant')
        elif self.sender().text() == 'Языки':
            self.second_form = Game(self, 'lang')
        self.second_form.show()
        ex.close()


class Game(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('game_interface.ui', self)
        self.mode = args[1]
        if self.mode == 'anim':
            self.lineEdit.insert('животного')
        elif self.mode == 'plant':
            self.lineEdit.insert('растения')
        elif self.mode == 'lang':
            self.lineEdit.insert('языка')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartPage()
    ex.show()
    sys.exit(app.exec_())