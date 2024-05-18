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
* В папке main_programm содержатся файлы с интерфейсом (game_interface.ui и start_page.ui), а также с основным алгоритмом () и алгоритмом взаимодействия с пользователем (main.py).
* В папке parsing лежат все питоновские скрипты, с помощью которых был произведен парсинг html-материалов.
   * animals_parsing.py (код для парсинга классификации животных с википедии)
   * id_languages.csv (айди языков с глоттолога, файл которых мы взяли в первом из ресурсов)
   * langs_parsing.py (неоконченный (_пока!_) код для парсинга глоттолога, с которым у нас возникли большие и мучительные проблемы)
   * languages_data.csv (однажды там появится файл с языковой классификацией)
   * plants_parcing.py (код для парсинга растений с википедии, который мы, не рассчитав время, не успели применить)


## Установка и использование

Воспользуйтесь pip, чтобы установить следующее:
```python
pip install sys
pip install PyQt5
pip install csv
pip install re
```
При написании кода также были использованы библиотеки bs4, request, pandas, numpy, но для корректной работы программы их установка необязательна.

Чтобы запустить программу, следует скачать файлы из папки main_programm.
```python
git clone https://github.com/PolinaHitrun/classy/tree/main.git
cd classy/main_programm
pip install -r requirements.txt
start "" python -m uvicorn api:app --reload 
start "" python -m http.server -d web 80 
```


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
