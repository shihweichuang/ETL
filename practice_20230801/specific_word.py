import requests
from bs4 import BeautifulSoup
import json

message = "2330.TW"

# 建立請求的URL(=欲爬取網站)
url = "https://tw.stock.yahoo.com/quote/" + str(message) + "/dividend"

# 設定請求標頭(模擬正常的瀏覽器行為)
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
    }

# 發送請求並獲取回應
res = requests.get(url,headers= headers)

# 設定編碼(防止中文亂碼)
res.encoding = "utf-8"

# 對獲取到的HTML內容進行解析
soup = BeautifulSoup(res.text,"html.parser")

soup1 = soup.find("div", {"class": "table-body-wrapper"})

# 爬取整個表格
list_n = soup.find("div", {"class": "table-body-wrapper"}).find_all("li", {"class": "List(n)"})
# 資料空字典
data_all = []

for i in range(len(list_n)):
    # 股利所屬期間
    period = list_n[i].find("div", {"class": "D(f) W(84px) Ta(start)"}).text
    # 現金股利+股票股利
    dividend = list_n[i].find_all("div", {
        "class": "Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(62px)"})
    # 現金股利
    cash_dividend = dividend[0].text
    # 股票股利
    stock_dividend = dividend[1].text
    # 除息日+除權日+現金股利發放日+股票股利發放日
    days = list_n[i].find_all("div", {
        "class": "Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(108px)"})
    # 除息日
    ex_dividend_date = days[0].text
    # 除權日
    ex_rights_date = days[1].text
    # 現金股利發放日
    cash_payment_date = days[2].text
    # 股票股利發放日
    stock_payment_date = days[3].text
    # 填息天數
    days = list_n[i].find_all("div",
                              {"class": "Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(70px)"})
    # 現金殖利率
    dividend_yield = days[0].text
    # 填息天數
    interest_date = days[1].text

    data_one = {
        "股利所屬期間": period,
        "現金股利": cash_dividend,
        "股票股利": stock_dividend,
        "除息日": ex_dividend_date,
        "除權日": ex_rights_date,
        "現金股利發放日": cash_payment_date,
        "股票股利發放日": stock_payment_date,
        "填息天數": interest_date
    }
    data_all.append(data_one)