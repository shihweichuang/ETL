import os # 加入目錄
import requests
from bs4 import BeautifulSoup
from load_article_tool import load_article

load_folder = 'articles'
if not os.path.exists(f'./{load_folder}'):
    os.mkdir(f'./{load_folder}')

url = 'https://www.ptt.cc/bbs/movie/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
}

for i in range(0, 5):
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    #Get all title tags
    title_tag_list = soup.select('div.title')

    for title_tag in title_tag_list:
        if title_tag.select_one('a'): # 如果不是空值，就跑以下內容
            title_name = title_tag.select_one('a').text
            article_url = 'https://www.ptt.cc' + title_tag.select_one('a')['href']
            try:
                load_article(
                    article_url=article_url,
                    load_path=f'./{load_folder}/{title_name}.txt',  # 另外製作一函數
                )
            except FileNotFoundError:
                load_article(
                    article_url=article_url,
                    load_path=f"./{load_folder}/{title_name.replace('/', '-')}.txt",
                )                                                    # 另外製作一函數
            except OSError:
                pass
            print(title_name)  # 印出所有標題
            print(article_url) # 印出所有網址
        else: # 如果是空值，就跑以下內容
            print('Title is empty.')

        print('======')

url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]