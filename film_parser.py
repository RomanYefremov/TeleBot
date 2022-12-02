import requests
from bs4 import BeautifulSoup


a = 1
for i in range(9):
    url = f'https://www.kinoafisha.info/rating/movies/?page={a}'
    headers = {
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    req = requests.get(url=url, headers=headers)
    sre = req.text
    soup = BeautifulSoup(sre, 'lxml')

    film_name = soup.find_all(class_="movieItem_title")

    with open('films.csv', 'a') as films:
        for k in film_name:
            k_text = k.text
            k_href = k.get('href')
            films.write(f'{k_text};{k_href}\n')

    a += 1
