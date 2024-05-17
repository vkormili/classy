from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://glottolog.org/glottolog/language'
page = requests.get(url)
filteredLanguages=[]
allLanguages=[]
soup = BeautifulSoup(page.text, "lxml")
table1 = soup.find('table', id='Families')
headers = []
for i in table1.find_all('tr'):
    title = i.text
    headers.append(title)
    #mydata = pd.DataFrame(columns=headers)
    mydata = pd.DataFrame(data=None, index=)
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row
print(mydata)
#mydata.to_csv('languages_data.csv', index=False)
    #mydata.drop(mydata.index[0:7], inplace=True)
    #mydata.drop(mydata.index[222:229], inplace=True)
    #mydata.reset_index(inplace=True, drop=True)
    #mydata.drop('#', inplace=True, axis=1)
#mydata.to_csv('languages_data.csv', index = False)
#mydata2 = pd.read_csv('languages_data.csv')
#allLanguages = soup.findAll('span', class_='level-language')
#for data in allLanguages:
    #if data.find('a', class_='Language') is not None:
        #filteredLanguages.append(data.text)
#for data in filteredLanguages:
    #print(data)

#animals = list(soup.findAll('li',class_=None, id_=None))[2:-15]
#for i in animals:
    #print(i)