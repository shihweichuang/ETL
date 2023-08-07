import requests
from bs4 import BeautifulSoup

# 目標網址
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

# 紀錄是否點擊過【已滿18歲】
cookies = {
    'over18': '1'
}

# 直接向目標網址發一個GET後看回應物件的text，同時加上傳入cookies，即可正確取得文章內容
res = requests.get(url, cookies=cookies)
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

arts = soup.find_all('div', {'class': 'r-ent'})

for art in arts:
    title = art.find('div', {'class': 'title'}).getText().strip()
    link = 'https://www.ptt.cc' + art.find('div', {'class': 'title'}).a['href'].strip()
    author = art.find('div', {'class': 'author'}).getText().strip()
    print(f'title: {title}\nlink: {link}\nauthor: {author}')