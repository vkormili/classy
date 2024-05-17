from bs4 import BeautifulSoup
import requests

url='https://glottolog.org/glottolog/language'
page = requests.get(url)
filteredlanguages=[]
alllanguages=[]
soup = BeautifulSoup(page.text, "html.parser")
alllanguages = soup.findAll('span', class_='level-language')
for data in alllanguages:
    if data.find('a', class_='Language') is not None:
        filteredlanguages.append(data.text)
for data in filteredlanguages:
    print(data)
#animals = list(soup.findAll('li',class_=None, id_=None))[2:-15]
#for i in animals:
    #print(i)