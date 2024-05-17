import csv
from bs4 import BeautifulSoup


with open('id_languages.csv', newline='') as csvfile:
    idreader = csv.reader(csvfile, delimiter=',')
    hrefs_list = []
    for row in idreader:
        hrefs_list.append('https://glottolog.org/resource/languoid/id/' + row[0])
    hrefs_list = hrefs_list[1:]

