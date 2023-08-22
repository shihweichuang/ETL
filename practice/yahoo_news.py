import requests
from bs4 import BeautifulSoup

stockNo = 2330

# 建立請求的URL(=欲爬取網站)
# https://tw.stock.yahoo.com/quote/2330/news
url = f"https://tw.stock.yahoo.com/quote/{stockNo}/news"

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

# 取得【相關新聞】區塊
soup1 = soup.find_all("h3", {"class": "Mt(0) Mb(8px)"}, limit = 13)

# 製作空清單，儲存標題及網址
title = []
address = []

# 將內容以迴歸方式儲存至清單中
for i in range(len(soup1)):
    # 排除掉廣告
    if i != 1 and i != 5 and i != 9:
        # 取出新聞網址
        new_ = soup1[i].find("a").get("href")
        address.append(new_)
        # 取出新聞標題
        title.append(soup1[i].text)