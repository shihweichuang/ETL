import requests
from bs4 import BeautifulSoup

stockNo = 2330

# 建立請求的URL(=欲爬取網站)
# https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID=2330
url = f"https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID={stockNo}"

# 設定請求標頭(模擬正常的瀏覽器行為)
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
        }

# 發送請求並獲取回應
res = requests.get(url,headers = headers)

# 設定編碼(防止中文亂碼)
res.encoding = "utf-8"

# 對獲取到的HTML內容進行解析
soup = BeautifulSoup(res.text,"html.parser")

# --------------取得【股票當日各價格】--------------

# 取得整個表格
soup1 = soup.find("table",{"class":"b1 p4_2 r10 box_shadow"})

# 取得表格中的文字(數值)：成交價、昨收、漲跌價、漲跌幅、振幅、開盤、最高、最低
# 最前後為空格，需剔除
soup2 = soup1.find("tr",{"align":"center"}).text.split(" ")[1:-1]

# 取得股票代碼及名稱
soup3 = soup.find("td", {"style": "padding:0 2px 5px 20px;width:10px;"})

# 取出股票代碼、股票名稱並分開文字
soup4 = soup3.find("a").text.split("\xa0")

# --------------取得【公司基本資料】--------------

# 取得【公司基本資料】表格
soup5 = soup.find("table",{"class":"b1 p4_4 r10 box_shadow"})

# 取得【公司基本資料】表格中的內容
soup6 = soup5.find_all("td", {"bgcolor": "white"})

# ---------------------------------------------

# 對獲取到的HTML內容進行解析
print(soup)
# 取得整個表格
print(soup1)
# 取得表格中的文字(數值)：成交價、昨收、漲跌價、漲跌幅、振幅、開盤、最高、最低
print(soup2)
# 取得股票代碼及名稱
print(soup3)
# 取出股票代碼、股票名稱並分開文字
print(soup4)
# 取得【公司基本資料】表格
print(soup5)
# 取得【公司基本資料】表格中的內容
print(soup6)