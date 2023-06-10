from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.ptt.cc/bbs/joke/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
} #自製一字典headers
#因為網頁被擋，會顯示HTTP Error 403，故需要再加一headers(user-agent)

req = request.Request(url=url, headers=headers) #請求的資料先打包成一物件
# res = request.urlopen(url=url) #不是要打開網址
res = request.urlopen(req)  #要打開一物件

html = res.read().decode('utf-8')

print(html)