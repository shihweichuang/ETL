import requests
from bs4 import BeautifulSoup

# ----------爬取網頁----------

# 連線至指定網頁
res = requests.get("https://isin.twse.com.tw/isin/C_public.jsp?strMode=2")

# print(res.text[:1000])

soup = BeautifulSoup(res.text,"html.parser")

# ----------將網頁轉成DataFrame----------

import pandas as pd        # 用於萃取原始碼，可操作各式各樣的表格，進行運算

df = pd.read_html(res.text)[0]         # 0 只抓第一張表格

# ----------整理資料：整理column名稱----------

# 設定column名稱
df.columns = df.iloc[0]
# 刪除第一行
df = df.iloc[1:]


# ----------整理資料：刪除冗餘行列----------

# 先移除row，再移除column，超過三個Nan則移除
df = df.dropna(thresh=3, axis=0). dropna(thresh=3, axis=1)

# ----------設定index----------

df = df.set_index('有價證券代號及名稱')