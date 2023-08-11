import requests
from bs4 import BeautifulSoup

cointype = input('請輸入幣種：')

url = f'https://www.google.com/search?q={cointype}'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
result = soup.find('span', class_='DFlfde SwHCTb')

# print(result)  # Output: <span class="DFlfde SwHCTb" data-precision="2" data-value="31.801000000000002">31.80</span>

if result:
    print(f'目前 1 {cointype}為 {result.text} 新台幣')  # Output: 目前 1 美金為 31.80 新台幣
else:
    print('目前沒有匯率')