from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 設定Chrome Driver的執行檔路徑
options = Options()
options.chrome_executable_path = 'chromedriver.exe'

# 建立Driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)

# 關閉瀏覽器
driver.close()