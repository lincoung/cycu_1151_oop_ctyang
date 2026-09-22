from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import Request, urlopen


def fetch_news_by_keyword(keyword='颱風'):
    url = 'https://news.tvbs.com.tw/'
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    try:
        with urlopen(request, timeout=10) as response:
            if response.status != 200:
                print(f'Failed to retrieve the news (HTTP {response.status})')
                return
            html = response.read()
    except Exception as error:
        print(f'Failed to retrieve the news: {error}')
        return

    soup = BeautifulSoup(html, 'html.parser')
    news_items = soup.find_all(['h2', 'h3'])
    found_news = 0

    print(f'篩選關鍵字：{keyword}')
    print('符合條件的新聞標題：')

    for item in news_items:
        title = item.get_text(' ', strip=True)
        if not title or keyword not in title:
            continue

        link_tag = item.find_parent('a', href=True)
        link = urljoin(url, link_tag['href']) if link_tag else url

        print(f'Title: {title}')
        print(f'Link: {link}')
        print('---')
        found_news += 1

    if found_news == 0:
        print('No news items found containing the keyword.')


if __name__ == '__main__':
    fetch_news_by_keyword('颱風')