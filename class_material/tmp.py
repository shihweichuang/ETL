import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
}
res = requests.get(url, headers = headers) #新增page

soup = BeautifulSoup(res.text, 'html.parser')

print(soup.select("a[class='btn wide']"))
print(
    'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]["href"]
)