import requests
import re
import json
from bs4 import BeautifulSoup

# 預期效果：爬取位於 http://ftp.ubuntu-tw.org/ubuntu-releases/ 的特定版本下載連結，並將其存放於 JSON 檔中。

version_list = ['14.04/', '16.04/', '18.04/', '20.04/', '22.04/', '23.04/']

# 預設網址
url = 'http://ftp.ubuntu-tw.org/ubuntu-releases/'

result_dict = {}

# 爬取特定版本下載連結
for version in version_list:
    # 發送請求，取得下載連結
    r = requests.get(url + version)
    # 解析頁面
    soup = BeautifulSoup(r.text, 'html.parser')
    desktop_iso = soup.find('a', string=re.compile(
        'ubuntu-\d{2}\.\d{2}\.?\d{0,2}-desktop-amd64\.iso'))['href']
    server_iso = soup.find('a', string=re.compile(
        'ubuntu-\d{2}\.\d{2}\.?\d{0,2}(-live)?-server-amd64\.iso'))['href']
    # 將下載網址以版本為key存到字典中
    result_dict[version] = {
        'desktop_iso': r.url + desktop_iso,
        'server_iso': r.url + server_iso
    }

# 將字典存於JSON檔案中
with open('iso-image.json', 'w', encoding = 'utf-8') as f:
    json.dump(result_dict, f, indent = 2,
              sort_keys = True, ensure_ascii = False)
