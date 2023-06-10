import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser') #BS需要一轉換器，不加會跑出警告文字

# print(soup)

logo_tag_object = soup.find('a', {'id': 'logo'})
# print(logo_tag_object) #印出 <a href="/bbs/" id="logo">批踢踢實業坊</a>

logo_tag_object_list = soup.findAll('a', {'id': 'logo'})
# print(logo_tag_object_list) #印出 [<a href="/bbs/" id="logo">批踢踢實業坊</a>]

logo_tag_object_list_2 = soup.findAll('a', id = 'logo')
# print(logo_tag_object_list_2) #印出 [<a href="/bbs/" id="logo">批踢踢實業坊</a>]

logo_tab_object = soup.select_one("a[id = 'logo']")
logo_tab_object_list = soup.select('a#logo')

print(logo_tab_object_list) #印出 [<a href="/bbs/" id="logo">批踢踢實業坊</a>]
print(logo_tab_object_list[0]) #取第一個字串 <a href="/bbs/" id="logo">批踢踢實業坊</a>
print(logo_tab_object_list[0].text) #印出 批踢踢實業坊
print('https://www.ptt.cc' + logo_tab_object_list[0]['href']) #印出連結 https://www.ptt.cc/bbs/

print('============================')

title_tag_list = soup.select('div.title') #returs a list of tag
# print(title_tag_list)
print("輸入: title_tag_list[0]\n", title_tag_list[0])
print("輸入:title_tag_list[0].find('a') \n", title_tag_list[0].find('a')) #印出 <a href="/bbs/joke/M.1677861895.A.C1E.html">Re: [猜謎] 新竹棒球場長香菇</a>
print("輸入: title_tag_list[0].find('a').text\n", title_tag_list[0].find('a').text) #印出 Re: [猜謎] 新竹棒球場長香菇
print("輸入: title_tag_list[0].find('a')['href']\n", title_tag_list[0].find('a')['href']) #印出 /bbs/joke/M.1677861895.A.C1E.html

print('============================')

print(type(soup)) # 印出 <class 'bs4.BeautifulSoup'>
print(type(title_tag_list[0].find('a'))) # 印出 <class 'bs4.element.Tag'>