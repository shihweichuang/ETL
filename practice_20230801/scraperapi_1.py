from scraper_api import ScraperAPIClient
from bs4 import BeautifulSoup

# 使用IP切換服務(ScraperAPI)
API_Key = 'cacb0907e22c9eedfe701a1c0788dc80'
client = ScraperAPIClient(API_Key)  # API Key

# 建立請求的URL(=欲爬取的網址)
url = 'https://tw.stock.yahoo.com/quote/2330/news'

# 設定請求標頭(模擬正常的瀏覽器行為)
headers = {
		'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
}

# 發送請求並獲取回應
res = client.get(url=url, headers=headers)

# 對獲取到的HTML內容進行解析
soup = BeautifulSoup(res.text, 'html.parser')

print(soup)