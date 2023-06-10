from selenium.webdriver import Chrome

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # 透過By來定位，對該標籤物件進行操作
import requests
from bs4 import BeautifulSoup

service = Service("./chromedriver")     # 呼叫chromedriver
driver = Chrome(service=service)        # seleniun內的chrome

# 要進入ptt八卦版，每次開啟時會是全新session
url = 'https://www.ptt.cc/bbs/index.html'

driver.get(url) # 打開ptt頁面
driver.find_element(by=By.CLASS_NAME, value='board-name').click()  # 指定定位點，click()進行點選
driver.find_element(by=By.CLASS_NAME, value='btn-big').click() # 指定定位點(我同意)

cookie = driver.get_cookies()

driver.close()

ss = requests.session()

# 設定cookies
for c in cookie:
    ss.cookies.set(c['name'], c['value'])

res = ss.get('https://www.ptt.cc/bbs/Gossiping/index.html')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())