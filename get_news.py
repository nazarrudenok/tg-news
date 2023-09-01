import requests
from bs4 import BeautifulSoup

url_ = None
def get_news(title: bool = False, href: bool = False, detailed: bool = False) -> str:
    url = 'https://tsn.ua/ato'

    r = requests.get(url).text
    bs = BeautifulSoup(r, 'html.parser')

    if title:
        data = bs.find_all('div', class_ = 'c-card__body')[0].find('h3').text
        return data
    elif href:
        data = bs.find_all('div', class_ = 'c-card__body')[0].find('a')['href']
        return data
    elif detailed:
        url2 = bs.find_all('div', class_ = 'c-card__body')[9].find('a')['href']

        r2 = requests.get(url2).text
        bs2 = BeautifulSoup(r2, 'html.parser')

        data = bs2.find('div', class_ = 'c-article__body').find_all('p')

        for i in range(len(data)):
            return f'<b>{data[0].text}</b>\n\n{data[1].text}\n\n{data[2].text}\n\n{data[4].text}'