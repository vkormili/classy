from bs4 import BeautifulSoup
import requests
import pandas as pd


def linkinator(anotherurl):  # часть 1, где объекты со страницы собираются в список, а мы пересматриваем финеса и ферба
    anotherlinkslist = []
    soup = BeautifulSoup(requests.get(anotherurl).text, "lxml")
    languages = list(soup.findAll('a', class_=None, id_=None))
    j = 0
    for link in languages:
        if j == 4 or j == 5:
            anotherlinkslist.append(link.get('href'))
            # print(link.get('title'), link.get('href'))
        if link.get('title') == 'Категория:Животные по алфавиту':
            j += 1
    return anotherlinkslist


def determinder(line, word):
    line_check = list(line.split(word)[1])
    j = 1
    answer = line_check[0]
    while ord(line_check[j]) >= 1072:
        answer += line_check[j]
        j += 1
    return answer


def classificator(link):
    turtle = 'https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D1%81%D1%82%D1%80%D0%B0%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B0' \
              '%D1%8F_%D0%B7%D0%BC%D0%B5%D0%B8%D0%BD%D0%BE%D1%88%D0%B5%D1%8F%D1%8F_%D1%87%D0%B5%D1%80%D0%B5%D0%BF%D0' \
              '%B0%D1%85%D0%B0 '
    if link == turtle:
        return 0
    name = pd.read_html(link, flavor='lxml')[0].columns.values[0]
    print(name)
    data = pd.read_html(link, flavor='lxml')[0][name][2]
    if 'Вид:' not in data or '†' in data:
        return [0, 0, 0, 0, 0, 0]
    species = data.split('Вид:')[1]
    genus = determinder(data, 'Род:')
    family = determinder(data, 'Семейство:')
    order = determinder(data, 'Отряд:')
    class_y = determinder(data, 'Класс:')
    phylum = determinder(data, 'Тип:')
    return [species, genus, family, order, class_y, phylum]


# print(classificator('https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D1%81%D1%82%D1%80%D0%B0%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D0%BE%D1%80%D0%BB%D1%8F%D0%BA'))
# print(classificator('https://ru.wikipedia.org/wiki/%D0%90%D0%B0%D1%80%D0%B4%D0%BE%D0%BD%D0%B8%D0%BA%D1%81'))
# print(classificator('https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D1%80%D0%BE%D1%80%D1%8B'))
# print(classificator('https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D1%81%D1%82%D1%80%D0%B0%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F_%D0%BA%D0%BE%D1%80%D0%B0%D0%BB%D0%BB%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BA%D0%BE%D1%88%D0%B0%D1%87%D1%8C%D1%8F_%D0%B0%D0%BA%D1%83%D0%BB%D0%B0'))

url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8' \
      '%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from=%D0%90 '

animals = pd.DataFrame(columns=['species', 'genus', 'family', 'order', 'class_y', 'phylum'])
while url != 'stop':
    linkslist = linkinator(url)
    for i in range(200):
        animals.append(classificator('https://ru.wikipedia.org' + linkslist[i]))
    url = 'https://ru.wikipedia.org' + linkslist[-1]
    if url == 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0' \
              '%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82' \
              '%D1%83&from=%D0%AF%D1%8E':
        break

animals.to_csv()
