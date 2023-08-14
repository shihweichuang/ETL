import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import json
import urllib.request


# 製作【股票資訊.csv】
def stock_info_csv(stockNo):
    # 取得今日日期
    now_date = datetime.now()

    # 格式化日期為"YYYYMMDD"
    formatted_now_date = now_date.strftime("%Y%m%d")

    # https://www.nstock.tw/api/v2/real-time-quotes/data?stock_id=2330
    url = f"https://www.nstock.tw/api/v2/real-time-quotes/data?stock_id={stockNo}"

    # 使用 urllib.request 套件來讀取網頁內容
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")

    # 解析 JSON 資料
    json_data = json.loads(data)

    # ------------取得【股票名稱】------------

    stock_info = "股票名稱"

    stock_name = json_data["data"][0][stock_info]

    # ------------取得【股票代號】------------

    stock_info = "股票代號"

    stock_no = json_data["data"][0][stock_info]

    stock_no = f"({stock_no})"

    # ---------取得【開盤價】---------

    stock_info = "開盤價"

    # 如果小數點後為0，只保留整數
    if json_data["data"][0][stock_info].split(".")[1] == "0000":
        open_price = json_data["data"][0][stock_info].split(".")[0]

    # 如果小數點後不為0，全部顯示
    else:
        open_price = json_data["data"][0][stock_info]

    # ---------取得【最高價】---------

    stock_info = "最高價"

    # 如果小數點後為0，只保留整數
    if json_data["data"][0][stock_info].split(".")[1] == "0000":
        high_price = json_data["data"][0][stock_info].split(".")[0]

    # 如果小數點後不為0，全部顯示
    else:
        high_price = json_data["data"][0][stock_info]

    # ---------取得【最低價】---------

    stock_info = "最低價"

    # 如果小數點後為0，只保留整數
    if json_data["data"][0][stock_info].split(".")[1] == "0000":
        low_price = json_data["data"][0][stock_info].split(".")[0]

    # 如果小數點後不為0，全部顯示
    else:
        low_price = json_data["data"][0][stock_info]

    # ---------取得【收盤價】---------

    stock_info = "當盤成交價"

    # 如果小數點後為0，只保留整數
    if json_data["data"][0][stock_info].split(".")[1] == "0000":
        close_price = json_data["data"][0][stock_info].split(".")[0]

    # 如果小數點後不為0，全部顯示
    else:
        close_price = json_data["data"][0][stock_info]

    # ----------取得【股價更新時間】----------

    stock_info = "最近交易日期"

    update_date = json_data["data"][0][stock_info]

    # 將日期轉換為datetime
    date_obj = datetime.strptime(update_date, "%Y-%m-%d")

    # 格式化為MMDD
    update_date = date_obj.strftime("%m/%d")

    stock_info = "最近成交時刻"

    update_time = json_data["data"][0][stock_info]

    update_date_time = f"{update_date} {update_time}"

    # -----------取得【漲跌】+【漲跌幅】-----------------

    stock_info = "漲跌"

    price_change = json_data["data"][0][stock_info]

    # 如果小數點後為0，只保留整數再加.00
    if price_change.split(".")[1] == "0000":
        price_change = price_change.split(".")[0] + ".00"

    # 如果小數點後不為0，顯示到小數點第二位(需先字串轉為浮點數)
    else:
        price_change = f"{float(price_change):.2f}"

    stock_info = "漲跌幅"

    # 取得漲跌幅(字串)
    price_change_rate = json_data["data"][0][stock_info]

    # 將漲跌幅(字串)轉為浮點數，用於符號判斷
    price_change_rate_test = float(price_change_rate)

    # 將漲跌幅(字串)轉為浮點數，再轉為字串
    price_change_rate = f"({float(price_change_rate)}%)"

    # 【漲跌價】符號判斷
    # 漲跌幅為正
    if price_change_rate_test > 0:
        price_change = "▲ " + price_change

    # 漲跌幅為0
    elif price_change_rate_test == 0:
        price_change = "- " + price_change

    # 漲跌幅為負
    elif price_change_rate_test < 0:
        price_change = "▼ " + price_change

    # -----------------進行爬蟲【產業名稱】---------------------------------------

    # https://www.nstock.tw/api/v2/basic-info/data?stock_id=2330
    url = f"https://www.nstock.tw/api/v2/basic-info/data?stock_id={stockNo}"

    # 使用 urllib.request 套件來讀取網頁內容
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")

    # 解析 JSON 資料
    json_data = json.loads(data)

    # -----------取得【產業名稱】-------------

    stock_info = "產業名稱"

    industry = json_data["data"][0][stock_info]

    # -----------------進行爬蟲【上市櫃】+【成交量】---------------------------------------

    # 建立請求的URL(=欲爬取網站)
    # https://www.nstock.tw/stock_info?status=1&stock_id=2330
    url = f"https://www.nstock.tw/stock_info?status=1&stock_id={stockNo}"

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

    # ----------------取得【上市櫃資訊】----------------
    soup1 = soup.find("span", {"class": "rounded-full border border-gray-400 p-0.5 px-2 overflow-clip"})
    text = soup1.text
    listing_cabinet = text.strip()

    # ------------取得【成交量】------------
    soup1 = soup.find_all("div", {"class": "text-base sm:text-2xl my-auto border-r border-gray-300 px-4 pr-2 sm:px-6"})
    text = soup1[0].find_all("div")[1].text
    deal_amount = text.strip()

    # ---------------將特定變數的值插入到字典中，再將字典轉換為DataFrame，再保存為csv---------------

    # 欄位名稱帶入變數
    var1 = update_date
    var2 = update_date_time
    var3 = stock_no
    var4 = stock_name
    var5 = listing_cabinet
    var6 = industry
    var7 = close_price
    var8 = price_change
    var9 = price_change_rate
    var10 = open_price
    var11 = high_price
    var12 = low_price
    var13 = deal_amount

    # 建立字典(每個值都用列表包起來，是為了將變數值轉換為DataFrame時符合格式要求)
    data = {
        "資料日期": [var1],
        "更新時間": [var2],
        "股票代碼": [var3],
        "股票名稱": [var4],
        "上市櫃": [var5],
        "產業別": [var6],
        "收盤價": [var7],
        "漲跌價": [var8],
        "漲跌幅": [var9],
        "開盤": [var10],
        "最高": [var11],
        "最低": [var12],
        "成交量": [var13]
    }

    # 將字典轉換為DataFrame對象
    df = pd.DataFrame(data)

    # 保存DataFrame為csv
    file_name = f"{stockNo}_info.csv"
    file_path = f"./{stockNo}_info.csv"
    df.to_csv(file_path, index=False, encoding="utf-8-sig")

    # 確認文字
    print("已完成 " + file_name)

stock_info_csv(2330)