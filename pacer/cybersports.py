from pprint import pprint

import requests
from bs4 import BeautifulSoup
import datetime

URL = "https://www.cybersport.ru/"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_="link_CocWY")
    cyber_news = []
    for item in items:
        date_from_html = item.find('time').get('datetime')
        date = datetime.datetime.strptime(date_from_html, "%Y-%m-%dT%H:%M:%S%z")
        cyber_news.append({
            "title": item.find('h2').string,
            "link": f"https://www.cybersport.ru{item.get('href')}",
            "description": item.find('p').string,
            "date_from_html": item.find('time').string,
            "date_python": date
        })
    return cyber_news


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        cyber_news = []
        for i in range(1, 2):
            html = get_html(f"{URL}page1_{i}.php")
            current_page = get_data(html.text)
            cyber_news.extend(current_page)
        return cyber_news
    else:
        raise Exception("Error in parser!")