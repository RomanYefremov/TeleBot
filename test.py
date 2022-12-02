import requests
from bs4 import BeautifulSoup


url = 'https://33tura.ru/goroda-ukrainy'
headers = {
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
req = requests.get(url=url, headers=headers)
sre = req.text

soup = BeautifulSoup(sre, 'lxml')
city_name = soup.find(class_='tur-article').find('table').find('tbody').find_all('td')
for i in city_name:
     textcity = i.text
     print(i.text)

