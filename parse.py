from bs4 import BeautifulSoup
import requests

url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
animals = list(soup.findAll('li',class_=None, id_=None))[2:-15]
for i in animals:
    print(i)