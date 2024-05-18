import random
import csv
import pandas as pd

# здесь можно все эти тройки прописывать в одной функции, но я не понимаю как из интерфейса вытащить что-то в переменную
# везде две версии, общая и для каждого мода отдельно

anim_base = open("probe.csv")
lang_base = open("probe.csv")
plant_base = open("probe.csv")

# эти инпуты нужно достать из ui

# mode = 'anim'
# userguess = 'Австралийская пятнистая макрель'

# загадываем что-то рандомом


# def ask_anim():
#     ask = random.choice(anim_base.readlines()).rstrip().split(';')
#     return ask
#
#
# def ask_lang():
#     ask = random.choice(lang_base.readlines()).rstrip().split(';')
#     return ask
#
#
# def ask_plant():
#     ask = random.choice(plant_base.readlines()).rstrip().split(';')
#     return ask


# это если мы можем вытащить мод в переменную сразу при выборе режима

def asking(mode):
    if mode == 'anim':
        base = anim_base
        ask = random.choice(base.readlines()).split(';')
    if mode == 'plant':
        base = plant_base
        ask = random.choice(base.readlines()).split(';')
    if mode == 'lang':
        base = lang_base
        ask = random.choice(base.readlines()).split(';')
    return ask


# достаем характеристику вида/языка из таблицы

# def guess_anim(userguess):
#     res = 0
#     for row in csv.reader(open('probe.csv')):
#         r = row[0].split(';')
#         if userguess == r[0]:
#             res = r
#     return res
#
# def guess_plant():
#     res = 0
#     for row in csv.reader(open('файл с растениями')):
#         r = row[0].split(';')
#         if userguess == r[0]:
#             res = r
#     return res
#
# def guess_lang():
#     res = 0
#     for row in csv.reader(open('файл с языками')):
#         r = row[0].split(';')
#         if userguess == r[0]:
#             res = r
#     return res

def guess(userguess, mode):
    if mode == 'anim':
        base = anim_base
    if mode == 'plant':
        base = plant_base
    if mode == 'lang':
        base = lang_base
        res = 0
    for row in csv.reader(base):
        r = row[0].split(';')
        if userguess == r[0]:
            res = r
    return res


# списки для сравнения генеалогии,
# записываем один раз при выборе режима
# a_anim = ask_anim()
# перезаписываем при каждом заполнении строки
# g_anim = guess_anim()

def proxi(a, g):
    proximity = 0
    if len(a) == len(g):
        for level in reversed(range(len(a))):
            if a[level] == g[level]:
                proximity += 1
    return proximity
