import requests

url = 'https://www.ptt.cc/bbs/joke/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
}

res = requests.get(url, headers=headers)

print(res) #印出 <Response [200]>

print(res.text) #印出 html字串
