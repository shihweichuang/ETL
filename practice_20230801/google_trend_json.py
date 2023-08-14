import requests
import json

# 建立請求的URL(=欲爬取網站)
url = 'https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&geo=TW&hl=zh-TW&ns=15'

# 發送請求並獲取回應
res = requests.get(url)

# 用字串的方式呈現
gettext = res.content

# 解析JSON
# 因開頭有多6個字元，json檔無法讀入，故需略過
getdata = json.loads(gettext[6:])