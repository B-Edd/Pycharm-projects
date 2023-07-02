import requests
from bs4 import BeautifulSoup

url = 'https://www.theweathernetwork.com/en/city/ca/ontario/milton/pollen'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='__next')
element = results.find_all("div", class_='sc-ba7d9f2b-3')
dictionary = {}
uv = set()
for i in element:
    title = i.find('div', class_='sc-ba7d9f2b-4 gnyYEw')
    pollen = i.find('span', class_='sc-ba7d9f2b-5 dBYwRc')
    airq = i.find('span', class_='sc-ba7d9f2b-5 eFlpqX')
    mold = i.find('span', class_='sc-ba7d9f2b-5 hZKTlr')

    pollen_element = pollen.text if pollen else None
    airq_element = airq.text if airq else None
    mold_element = mold.text if mold else None

    if pollen is not None:
        dictionary['Pollen: '] = pollen.text
    if airq is not None:
        dictionary['Air quality: '] = airq.text
    if mold is not None:
        dictionary['Mold: '] = mold.text

for i in dictionary:
    print(i + dictionary[i])
