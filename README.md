# classy
_"feel the classification!"_

## Описание
### Идея
**classy** — это десктопное приложение, представляющее из себя игру-угадайку на основе классификации с несколькими режимами:
* животные
* растения (скоро)
* языки (чуть менее скоро)

Мы вдохновлялись [контекстно.рф](https://xn--e1ajbkccewgd.xn--p1ai/random), [wordle](https://www.nytimes.com/games/wordle/index.html) и [spotle](https://spotle.io/). Все они облегчают игру с помощью подсказок, которые позволяют игроку понять, насколько он близок к разгадке.

### Структура репозитория
* В папке main_programm содержатся файлы:
  * game_interface.ui и start_page.ui (с интерфейсом)
  * functions.py (основной алгоритм)
  * main.py (алгоритм взаимодействия с пользователем)
  * animals.csv (файл с классификацией животных в результате верстки)
  * requirements.txt (файл со всеми библиотеками для установки)
* В папке parsing лежат все питоновские скрипты, с помощью которых был произведен парсинг html-материалов.
   * animals_parsing.py (код для парсинга классификации животных с википедии)
   * animals_resultofparcing.csv (файл с классификацией животных по результату парсинга)
   * id_languages.csv (айди языков с глоттолога, файл которых мы взяли в первом из ресурсов)
   * langs_parsing.py (неоконченный (_пока!_) код для парсинга глоттолога, с которым у нас возникли большие и мучительные проблемы)
   * languages_data.csv (однажды там появится файл с языковой классификацией)
   * plants_parcing.py (код для парсинга растений с википедии, который мы, не рассчитав время, не успели применить)


## Установка и использование
Потребуется версия python >= 3.9
### Как скачать
Чтобы запустить программу, следует скачать файлы из папки main_programm и запустить файл main.py или выполнить следующие команды:
```python
git clone https://github.com/PolinaHitrun/classy
cd classy/main_programm
pip install -r requirements.txt
python main.py
```
Если у вас по какой-то причине не скачалась какая-либо библиотека из тех, что содержатся в requirements.txt, можете попробовать скачать их самостоятельно. Например, с помощью пайчарма: Меню — Settings — Project — Python Interpreter (Project Interpreter).

Или отсюда с помощью pip, если проблема именно с PyQt5
```python
-m pip install PyQt5
-m pip install --upgrade pip #если необходимо
```
### Как играть
1. У вас должно открыться приветственное окно с выбором из нескольких режимов. Так как на данный момент полностью доработана категория животных, нажмите на нее.
2. Появится окно самой игры. Введите в поисковую строку (белая горизонтальная полоска в верху окна) вашу догадку (на панели справа будут предлагаться варианты ответов в зависимости от введенных символов).
3. Для каждого введенного ответа вы можете отслеживать прогресс (то, насколько близко ваша отгадка по классификации к загаданному) на шкале прогресса. То есть по мере заполнения шкалы вы можете видеть, на каком уровне классификации совпадает введенный вид животного с загаданным. Ваши ответы будут сохранены в разделе "Предыдущие ответы".
4. Если животное будет отгадано, внизу высветится надпись о том, что вы победили. А также шкала будет заполнена на 100%.
### Приятного использования!


## Участники
* Кормилицына Варвара 232
* Хитрун Полина 233
* Шванова Инна 233
* Попова Юлия 233
* Зайцева Елизавета 232
## Ресурсы
* https://github.com/glottolog/glottolog-cldf/blob/master/cldf/languages.csv
* https://habr.com/ru/articles/544828/
* https://habr.com/ru/companies/ruvds/articles/494720/
## Контакт для [обратной] связи
[@polinahitrun](https://t.me/polinahitrun)
