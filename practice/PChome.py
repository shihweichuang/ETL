import requests
import json
import pandas as pd
import time

keyword = '櫃子'

# --------------爬取第一頁的結果--------------

# 建立請求的URL(=欲爬取網站)
# https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E9%9E%8B%E6%AB%83&page=2&sort=rnk/dc
url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=' + keyword + '&page=1&sort=rnk/dc'

# 發送請求並獲取回應
res = requests.get(url)

# 解析JSON
getdata = json.loads(res.content)

# --------------爬取多頁的結果--------------

# ----------蒐集多頁的資料，打包成csv檔案----------
# 準備一個容器
alldata = pd.DataFrame()

# 爬取從第1頁到第10頁
for i in range(1, 11):
    # 建立請求的URL(=欲爬取網站)
    # https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E9%9E%8B%E6%AB%83&page=2&sort=rnk/dc
    url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=' + keyword + '&page=' + str(i) + '&sort=rnk/dc'

    # 發送請求並獲取回應
    res = requests.get(url)

    # 解析JSON
    getdata = json.loads(res.content)

    # 轉成DataFrame格式
    todataFrame = pd.DataFrame(getdata['prods'])

    # 將結果裝進容器
    alldata = pd.concat([alldata, todataFrame])

    # 拖延時間(避免密集要求被封鎖)
    time.sleep(5)

# ----------儲存檔案----------
alldata.to_csv('PChome.csv',         # 名稱
               encoding='utf-8-sig', # 編碼
               index=False)          # 是否保留Index