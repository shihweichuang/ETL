import pandas as pd
import requests
import json
import datetime
from dateutil.relativedelta import relativedelta
import time
import random
import tqdm

# https://tianqi.2345.com/
areaId = '71294'   # 台北
areaType = '2'
year = '2023'
month = '8'
# 要抓取的網址
url = 'https://tianqi.2345.com/Pc/GetHistory?areaInfo%5BareaId%5D=' + str(areaId) + '&areaInfo%5BareaType%5D=' + str(areaType) + '&date%5Byear%5D=' + str(year) + '&date%5Bmonth%5D=' + str(month)
# 請求網站
res = requests.get(url)
# 將網站程式碼爬下來
# 為HTML(table)
getJson = json.loads(res.content)
# 抓到資料
getTable = pd.read_html(getJson['data'], header=0)

# -----取得大量資料，該地區12個月-----
# 取得現在日期
today = datetime.datetime.today()
areaId = '71294'   # 台北
areaType = '2'
# 準備一個容器(每爬取一個月，就儲存到容器)
container = pd.DataFrame()
# tqdm可設定進度條(做大量時不建議使用)
for i in tqdm.tqdm(range(3)):
    # 計算的目標時間的年份、月份
    countDay = today - relativedelta(months=i)
    year = countDay.year
    month = countDay.month
    # 要抓取的網址
    url = 'https://tianqi.2345.com/Pc/GetHistory?areaInfo%5BareaId%5D=' + str(areaId) + '&areaInfo%5BareaType%5D=' + str(areaType) + '&date%5Byear%5D=' + str(year) + '&date%5Bmonth%5D=' + str(month)
    # 請求網站
    print(str(i) + '開始請求')
    res = requests.get(url)
    print(str(i) + '請求完成')
    # 將整個網站的程式碼爬下來
    getJson = json.loads(res.content)
    # 使用pandas爬蟲轉換為Table
    getTable = pd.read_html(getJson['data'], header=0)
    # 合併資料
    container = pd.concat([container, getTable[0]])
    # 休息一下(網站可能會擋)，每次休息秒數隨機
    time.sleep(random.randint(45, 70))

container.to_csv('台北天氣情況.csv',
                 encoding='utf-8-sig',
                 index=False)