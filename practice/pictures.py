# --------------爬取圖片來源網址--------------

import requests                # 發送請求給網頁
from bs4 import BeautifulSoup  # 爬取回應的結果之內容
import os                      # 提供操作檔案及目錄的方法，可以協助建立資料夾及存放下載的圖片

input_image = input("請輸入要下載的圖片(需輸入英文)：")

# 請求圖片網址
url = f"https://unsplash.com/s/photos/{input_image}"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
    }

res = requests.get(url, headers=headers)

# 進行解析
soup = BeautifulSoup(res.text, "html.parser")

# 爬取所有指定樣式類別(class)的圖片標籤
# 需要取得的圖片數量
limit = 5
results = soup.find_all("img", {"class": "tB6UZ a5VGX"}, limit=limit)

# 取得圖片來源連結
image_links = [result.get("src") for result in results]

# --------------下載圖片至資料夾中--------------

# 下載圖片時要以使用者輸入的文字+迴圈索引值來命名圖檔
for index, link in enumerate(image_links):

    # 如果該專案資料夾下沒有資料夾(images)
    if not os.path.exists("images"):
        # 如果沒有，建立資料夾
        os.mkdir("images")

    # 下載圖片
    img = requests.get(link)

    # 打開資料夾，並命名圖檔
    with open("images\\" + input_image + str(index+1) + ".jpg", "wb") as file:
        # 指定寫入圖片的二進位碼(wb)，直到所有圖片接寫入完畢，自動關閉資料夾，釋放資源
        file.write(img.content)