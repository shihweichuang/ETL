import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

#Get all title tags
title_tag_list = soup.select('div.title')

for title_tag in title_tag_list:
    # print(title_tag)
    title_name = title_tag.select_one('a').text
    article_url = 'https://www.ptt.cc' + title_tag.select_one('a')['href']
    print(title_name)  # 印出所有標題
    print(article_url) # 印出所有網址
    print('======')