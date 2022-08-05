import requests
import bs4
import re
import time

HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1135853753.1652457614; hl=ru; fl=ru; _ym_d=1655113943; _ym_uid=16551139431039354769; '
              'habr_web_home_feed=/all/; _ym_isad=2; _gid=GA1.2.262726070.1659551025; _gat_gtag_UA_726094_1=1',
    'Host': 'habr.com',
    'If-None-Match': 'W/"2d72-jB67kFF5xFKvrjv8niN9WMH/YbM"',
    'Referer': 'https://habr.com/ru/all/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36',
    'x-app-version': '2.84.0'
}

KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'компании', 'привет', 'бизнесу'}


def main():
    response = requests.get('https://habr.com/ru/all/', headers=HEADERS).text
    soup = bs4.BeautifulSoup(response, features='html.parser')
    articles = soup.find_all('article', class_='tm-articles-list__item')

    pattern = "|".join(KEYWORDS)

    for article in articles:
        time_article = article.find('time').attrs['title']
        title = article.find('h2').find('span').text
        href = 'https://habr.com' + article.find('h2').find('a').attrs['href']
        prews = article.find('div', class_='tm-article-body tm-article-snippet__lead').find_all('p')
        preview = ''
        for prew in prews:
            preview = preview + prew.text
        text = get_text(href)
        if len(re.findall(pattern, preview)) > 0 or len(re.findall(pattern, text)):
            print(f'Время: {time_article}')
            print(f'Заголовок - {title}')
            print(f'Ссылка - {href}')
            print('=' * 50)


def get_text(href):
    text = ""
    time.sleep(2)
    response = requests.get(href, headers=HEADERS).text
    soup = bs4.BeautifulSoup(response, features='html.parser')
    paragraphs = soup.find('div', id='post-content-body').find_all('p')
    for item in paragraphs:
        text = text + item.text
    return text


if __name__ == "__main__":
    main()
