import requests
from bs4 import BeautifulSoup

def fetch_tvbs_news():
    url = 'https://news.tvbs.com.tw/'
    response = requests.get(url)
    response.encoding = 'utf-8'
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.find_all('div', class_='news_list')
        
        for item in news_items:
            title = item.find('h2').text.strip()
            link = item.find('a')['href']
            print(f'Title: {title}')
            print(f'Link: {link}')
            print('---')
    else:
        print('Failed to retrieve the news')

if __name__ == "__main__":
    fetch_tvbs_news()