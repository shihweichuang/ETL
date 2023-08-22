import requests
import json
from bs4 import BeautifulSoup

# 定義一串列，存放所有文章資訊
article_list = []


def get_res(url):
    cookies = {
        'over18': '1'
    }
    res = requests.get(url, cookies=cookies)
    if res.status_code != 200:
        return 'error'
    else:
        return res


def get_articles(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    arts = soup.find_all('div', class_='r-ent')

    for art in arts:
        title = art.find('div', class_='title').getText().strip()

        # 避免文章刪除而無法爬取文章連結，加上判斷式解決
        if not title.startswith('(本文已被刪除)'):
            link = 'https://www.ptt.cc' + \
                   art.find('div', class_='title').a['href'].strip()

        author = art.find('div', class_='author').getText().strip()
        article = {
            'title': title,
            'link': link,
            'author': author
        }
        article_list.append(article)
        # print(f'title: {title}\nlink: {link}\nauthor: {author}')

    # 利用Css Selector定位下一頁網址
    next_url = 'https://www.ptt.cc' + \
               soup.select_one(
                   '#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)'
               )['href']
    return next_url


# 當執行此程式時成立
if __name__ == '__main__':
    # 第一個頁面網址
    url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
    # 先讓爬蟲爬10頁
    for now_page_number in range(10):
        print(f'crawing {url}')
        res = get_res(url)
        if res != 'error':
            url = get_articles(res)
        print(f'======{now_page_number + 1}/10======')
    # 將存放所有文章資訊的串列存於JSON檔案中
    with open('ptt-articles.json', 'w', encoding='utf-8') as f:
        json.dump(article_list, f, indent=2,
                  sort_keys=True, ensure_ascii=False)