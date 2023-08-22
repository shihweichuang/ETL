from scraper_api import ScraperAPIClient

# 使用IP切換服務
API_Key = input('請輸入API Key：')
client = ScraperAPIClient(API_Key)  # API Key
result = client.get(url = 'https://httpbin.org/ip')

# -------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

# 設定Chrome Driver的執行檔路徑
options = Options()

# User-Agent設定
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# 繞過JavaScript渲染的設定
options.add_argument("--disable-blink-features=AutomationControlled")

# 設定捲動視窗次數
scroll_time = int(input('請輸入想要捲動幾次：'))

# 建立Driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)

# 開始連線到網址
url = 'https://www.dcard.tw/f/talk'   # 目標網址
# url = 'https://www.dcard.tw/f/talk?latest=true'   # 目標網址

# url = 'https://id.dcard.tw/oauth/login?redirect=%2Foauth%2Fauthorize%3Fbdid%3Dadefec66-f642-453a-84ba-2ee86807b10a%26client_id%3Dc2e76395-38a1-48f7-a9e0-af735b8f7c41%26code_challenge%3DoOwXPsxXAFgykw5t-BCJvff83gXruRE6tcxCSFDSiPc%26code_challenge_method%3DS256%26display%3Dpage%26login_type%3Demail%26max_age%3DNaN%26product%3DDcard%26redirect_uri%3Dhttps%253A%252F%252Fwww.dcard.tw%252Fservice%252F_auth%252Fcallback%26region%3DTW%26response_type%3Dcode%26scope%3Dconfig%2520config%253Awrite%2520device%2520device%253Awrite%2520email%2520email%253Awrite%2520facebook%2520feed%253Asubscribe%2520forum%2520forum%253Asubscribe%2520idcard%2520member%2520member%253Awrite%2520notification%2520persona%2520phone%2520phone%253Avalidate%2520phone%253Awrite%2520photo%2520post%2520post%253Asubscribe%2520topic%2520topic%253Asubscribe%2520collection%2520collection%253Awrite%2520comment%253Awrite%2520forum%253Awrite%2520friend%2520friend%253Awrite%2520identity%253Avalidated%2520like%2520downvote%2520reaction%2520match%2520match%253Awrite%2520message%2520message%253Awrite%2520message%253Aprivate%2520poll%253Awrite%2520persona%253Asubscribe%2520persona%253Awrite%2520post%253Awrite%2520report%2520token%253Arevoke%2520loginVerification%2520loginVerification%253Averify%26state%3DeyJjc3JmIjoieXFRalZWYTMtNXNwUEVpNkpfWDF6azg0TXl2LTBOSlhwSDFJIiwicmVkaXJlY3QiOiIvc2VydmljZS9zc28vY2FsbGJhY2s_cmVkaXJlY3Q9JTJGZiUyRnRhbGsifQ%26ui_locales%3Dzh-TW&ui_locales=zh-TW&display=page&login_type=email&product=Dcard&region=TW&bdid=adefec66-f642-453a-84ba-2ee86807b10a'   # 目標網址
driver.get(url)

# 視情況調整睡眠時間
sleep(120)

# 捲動視窗並等待瀏覽器載入更多內容
for now_time in range(1, scroll_time+1):                                                                  # 執行3次
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # 捲動視窗到底部
    sleep(3)                                                                  # 等待3秒鐘

# 取得網頁原始碼(確認用)
all_page = driver.page_source

# 關閉瀏覽器
driver.close()

# ---------------------------------------------

from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(all_page, 'html.parser')
elements = soup.find_all('a', class_='atm_cs_1urozh')

# -------------取得【文章標題、文章連結】-------------

title_list = []
link_list = []

for ele in elements:
    title = ele.span.get_text()
    title_list.append(title)
    link = 'https://www.dcard.tw' + ele['href']
    link_list.append(link)

# -------------取得【心情數量】-------------

emotion_amount = []

elements = soup.find_all('div', class_='atm_lk_i2wt44 c1jkhqx5')
for ele in elements:
    emotion = ele.text
    emotion_amount.append(emotion)

# -------------取得【留言數量】-------------

elements = soup.find_all('div',
                         class_='atm_9s_1txwivl atm_h_1h6ojuz atm_ll_exct8b atm_dz43bx_idpfg4 atm_1pqnrs9_gktfv atm_1dlbvfv_gktfv atm_1in2ljq_i2wt44 atm_leio7s_81a4vn fnja3xi')

message_amount = []  # 用於儲存輸出的數字

odd_index = 0  # 奇數索引(控制打印奇數個數字)
for index, ele in enumerate(elements):
    number_span = ele.find('span')
    number = number_span.text.strip()  # 删除內容中的額外空格和換行符號

    if number and number != '收藏':  # 排除空白和"收藏"文本
        odd_index += 1
        if odd_index % 2 == 1:  # 只印出奇數索引的內容
            message_amount.append(number)

# ---------------製作【資料集】---------------

results = []

for i in range(len(title_list)):
    result = {
        'title': title_list[i],
        'link': link_list[i],
        'emotion': emotion_amount[i],
        'message': message_amount[i]
    }
    results.append(result)

print(results)

# ---------------另存成JSON---------------
with open('Dcard-articles0822.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2,
              sort_keys=True, ensure_ascii=False)