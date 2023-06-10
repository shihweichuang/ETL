import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index{}.html' #因為要爬很多頁，index後加入{}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
}

page = 9514

#以下包進一個迴圈
for i in range(0, 5):
    res = requests.get(url.format(page), headers=headers) #新增page

    soup = BeautifulSoup(res.text, 'html.parser')

    #Get all title tags
    title_tag_list = soup.select('div.title')

    for title_tag in title_tag_list:
        # print(title_tag)
        # try:                 #因有問題，故新增try except
        #     title_name = title_tag.select_one('a').text
        #     article_url = 'https://www.ptt.cc' + title_tag.select_one('a')['href']
        #     print(title_name)  # 印出所有標題
        #     print(article_url) # 印出所有網址
        # except AttributeError as e:
        #     print(title_tag)
        #     # 因含空值，改以if/else處理
        if title_tag.select_one('a'): # 如果不是空值，就跑以下內容
            title_name = title_tag.select_one('a').text
            article_url = 'https://www.ptt.cc' + title_tag.select_one('a')['href']
            print(title_name)  # 印出所有標題
            print(article_url)  # 印出所有網址
        else: # 如果是空值，就跑以下內容
            print('Title is empty')

        print('======')

    page -= 1 #回到上一頁