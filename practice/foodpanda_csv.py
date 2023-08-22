import requests
from bs4 import BeautifulSoup
import pandas as pd

# 建立請求的URL(=欲爬取網站)
url = 'https://www.foodpanda.com.tw/city/new-taipei-city'

# 設定請求標頭(模擬正常的瀏覽器行為)
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
}

# 發送請求並獲取回應
res = requests.get(url, headers=headers)

# 設定編碼(防止中文亂碼)
res.encoding = 'utf-8'

# 對獲取到的HTML內容進行解析
soup = BeautifulSoup(res.text, 'html.parser')

# 取得所有商家的所有資訊
all_info = soup.find_all('figcaption', {'class': 'vendor-info'})

# 取得第一個商家的所有資訊
first = all_info[0]

# 確認是否有參雜別的內容，印出所有商家的店名
for i in all_info:
    print(i.find('span', {'class': 'name fn'}))

# 取得第一家的商家名稱
name = first.find('span', {'class': 'name fn'}).text

# 取得商家的評分
score = first.find('span', {'class': 'rating--label-primary cl-rating-tag-text f-label-small-font-size fw-label-small-font-weight lh-label-small-line-height'} ).text
# 適當處理取出內容
score = score.split('/')[0]

# 取得商家的標籤
label = first.find('li', {'class': 'vendor-characteristic'} ).text

# 整理成資料表
shopName = []
label = []
for i in all_info:
    shopName.append(i.find('span', {'class': 'name fn'}).text)
    label.append(i.find('li', {'class': 'vendor-characteristic'} ).text)

star = []
for i in all_info:
    star.append(i.find('span', {'class': 'rating--label-primary cl-rating-tag-text f-label-small-font-size fw-label-small-font-weight lh-label-small-line-height'}))

ratings = []

for star_ele in star:
    # 如果元素是 None
    if star_ele is None:
        # 設定為無評分
        rating = '無評分'
        ratings.append(rating)
    # 如果元素不是 None
    else:
        # 獲取評分文本，例如 '3.3/5'
        rating_text = star_ele.get_text()
        # 分割文本，取得 '3.3'
        rating = rating_text.split('/')[0]
        ratings.append(rating)

# 將資料轉成DataFrame及CSV檔

pd.DataFrame({
    '店家名稱': shopName,
    '評分': ratings,
    '標籤': label,
}).to_csv('foodpanda.csv', encoding='utf-8-sig', index=False) # 不顯示index