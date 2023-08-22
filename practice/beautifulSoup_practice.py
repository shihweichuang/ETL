import requests
from bs4 import BeautifulSoup

url = 'https://ithelp.ithome.com.tw/users/20134430/ironman/4307'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

# 發送GET請求到url，並將回應物件存到res
res = requests.get(url, headers=headers)

# 將res.text=HTML資料定義到BeautifulSoup物件內，並用html.parser解析HTML內容
soup = BeautifulSoup(res.text, 'html.parser')

# 輸出網頁的 title
print(soup.title.getText())

# 輸出第一個尋找到的<li>元素的文字
print(soup.li.getText())

# 輸出第一個尋找到的<li>元素的文字(效果相同)
print(soup.find('li').getText())

# 尋找全部<li>元素的文字
lis = soup.find_all('li')
for li in lis:
    print(li.getText())

# -------------------取得標籤屬性-------------------

import requests
from bs4 import BeautifulSoup

url = 'https://ithelp.ithome.com.tw/users/20134430/ironman/4307'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

# 發送GET請求到url，並將回應物件存到res
res = requests.get(url, headers=headers)

# 將res.text=HTML資料定義到BeautifulSoup物件內，並用html.parser解析HTML內容
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.find_all('a')
for link in links:
    if 'href' in link.attrs:
        print(link['href'])

# -------------------BeautifulSoup定位-------------------

import requests
from bs4 import BeautifulSoup

url = 'https://ithelp.ithome.com.tw/users/20134430/ironman/4307'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

# 發送GET請求到url，並將回應物件存到res
res = requests.get(url, headers=headers)

# 將res.text=HTML資料定義到BeautifulSoup物件內，並用html.parser解析HTML內容
soup = BeautifulSoup(res.text, 'html.parser')

# 取得網址
link = soup.find('a', class_='qa-list__title-link')
print(link['href'].strip())