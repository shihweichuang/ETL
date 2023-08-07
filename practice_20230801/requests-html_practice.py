from requests_html import HTMLSession

# 宣告Session
session = HTMLSession()

r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')
print(type(r.html))     # Output: <class 'requests_html.HTML'>

r = session.post('https://ithelp.ithome.com.tw/users/20134430/ironman/4307', data={})
print(type(r.html))     # Output: <class 'requests_html.HTML'>

# --------------------資料清洗--------------------

from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')

# 輸出網頁的網址
print(r.html.url)    # Output: https://ithelp.ithome.com.tw/users/20134430/ironman/4307

# 輸出網頁內容內的所有網址
print(r.html.links)

# 輸出網頁內容(HTML)
print(r.text)

# 輸出網頁文字內容(除去HTML)
print(r.html.text)

# ------------------使用find------------------

from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')

ele = r.html.find(
    'body > div.container.index-top > div > div > div.board.leftside.profile-main > div.ir-profile-content')

print(ele[0].text)

# ------------------使用xpath------------------

from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')

ele = r.html.xpath(
    '/html/body/div[2]/div/div/div[2]/div[1]')

print(ele[0].text)

# ------------------使用search------------------

from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')

# print(r.html.text)

ele = r.html.xpath(
    '/html/body/div[2]/div/div/div[2]/div[1]')

print(ele[0].search('【Day {}】'), ele[0].search('【Day {}】').fixed)

# ------------------使用search_all------------------

from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')

# print(r.html.text)

ele = r.html.xpath(
    '/html/body/div[2]/div/div/div[2]/div[1]')

print(ele[0].search_all('【Day {}】'))

for day in ele[0].search_all('【Day {}】'):
    print(day.fixed)