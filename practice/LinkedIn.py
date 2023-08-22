# 載入相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 設定Chrome Driver的執行檔路徑
options = Options()
# options.chrome_executable_path='chromedriver.exe'

# 建立Driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)

# 要連線的網址
url = 'https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0'

# 連線到 LinkedIn 工作搜尋網頁
driver.get(url)

# 捲動視窗並等待瀏覽器載入更多內容
n = 0
while n < 3:  # 執行3次
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # 捲動視窗到底部
    time.sleep(3)  # 等待3秒鐘
    n += 1

# 取得網頁中的工作的標題
title_list = []
titleTags = driver.find_elements(By.CLASS_NAME, 'base-search-card__title')
for titleTag in titleTags:
    title_list.append(titleTag.text)

# 取得網頁中的工作的副標題
subtitle_list = []
subtitleTags = driver.find_elements(By.CLASS_NAME, 'base-search-card__subtitle')
for subtitleTag in subtitleTags:
    subtitle_list.append(subtitleTag.text)

# 取得網頁中的工作的地區
location_list = []
locationTags = driver.find_elements(By.CLASS_NAME, 'job-search-card__location')
for locationTag in locationTags:
    location_list.append(locationTag.text)

# 取得網頁中的工作的更新日期
updatetime_list = []
updatetimeTags = driver.find_elements(By.CLASS_NAME, 'job-search-card__listdate--new')
for updatetimeTag in updatetimeTags:
    updatetime_list.append(updatetimeTag.text)

# 印出清單結果
for i in range(len(title_list)):
    print(title_list[i])
    print(subtitle_list[i])
    print(location_list[i])
    print(updatetime_list[i])
    print('=' * 50)

# 關閉瀏覽器
driver.close()