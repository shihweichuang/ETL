from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 設定Chrome Driver的執行檔路徑
options = Options()
options.chrome_executable_path = 'chromedriver.exe'

# 建立Driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)

# ----------取得PTT股票版中的文章標題----------

# 開始連線到網址
url = 'https://www.ptt.cc/bbs/Stock/index.html'   # 目標網址
driver.get(url)

# # 取得網頁原始碼
# print(driver.page_source)

tags = driver.find_elements(By.CLASS_NAME, 'title')  # 搜尋 class 屬性是 title 的所有標籤
# 印出所有標籤之文字內容
for tag in tags:
    print(tag.text)

# ----------取得上一頁的文章標題----------
link = driver.find_element(By.LINK_TEXT, '‹ 上頁')
link.click()   # 模擬使用者點擊連結標籤
tags = driver.find_elements(By.CLASS_NAME, 'title')  # 搜尋 class 屬性是 title 的所有標籤
# 印出所有標籤之文字內容
for tag in tags:
    print(tag.text)


# 關閉瀏覽器
driver.close()