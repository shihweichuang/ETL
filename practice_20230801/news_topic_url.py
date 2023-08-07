# 爬取【鉅亨網-頭條新聞-標題+網址】

import requests
from bs4 import BeautifulSoup

# 建立請求的URL(=欲爬取網站)
url = "https://news.cnyes.com/news/cat/headline"

# 設定請求標頭(模擬正常的瀏覽器行為)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
}
# 發送請求並獲取回應
res = requests.get(url, headers=headers)

# 設定編碼(防止中文亂碼)
res.encoding = "utf-8"

# 對獲取到的HTML內容進行解析
soup = BeautifulSoup(res.text, "html.parser")

# 在find_all中的第二個參數做輸入，縮小搜尋範圍
# limit = 10 只抓取10筆
soup1 = soup.find_all("a", {"class": "_1Zdp"}, limit=10)

# 網址基礎，用於建構完整的網址
base = "https://news.cnyes.com"

# 建立空的標題和地址列表，用於儲存標題和地址的資訊
title = []
address = []

# 利用迴圈將新聞標題、網址抓取下來
for i in soup1:
    title.append(i.get("title"))
    address.append(base + i.get("href"))

# 新聞標題
print(title)
print('=====================')
# 新聞網址
print(address)