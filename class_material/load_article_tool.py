import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
}

def load_article(article_url: str, load_path: str):
    '''
    1. request article page
    2. beautifulsoup object
    3. select article part
    4. load article text
    '''
    res = requests.get(article_url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    article_tag = soup.select_one('div[id="main-content"]') # 定位文章部分
    for tag in article_tag.select('div'): # 刪除指定部分
        tag.extract()
    # print(article_tag)
    article_content = article_tag.text # 轉為文字
    with open(load_path, 'w', encoding='utf-8') as f: # load_path為儲存路徑
        f.write(article_content)
    # print('==================')
    # print(article_tag.select_one("div[class='article-metaline]").extract() # 移除不要的標籤
    # print('==================')
    # print(article_tag)
    pass

if __name__=='__main__':
    article_url = 'https://www.ptt.cc/bbs/movie/M.1677862363.A.7AE.html'
    load_article(article_url, './test.txt')