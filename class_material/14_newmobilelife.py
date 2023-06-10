import requests
import pprint
from bs4 import BeautifulSoup


headers = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"
}

url = "https://www.newmobilelife.com/wp-json/csco/v1/more-posts"

data_str = '''action: csco_ajax_load_more
page: 4
posts_per_page: 30'''

data = {row.split(": ")[0]: row.split(": ")[1] for row in data_str.split("\n")} # 將字串轉為字典，action為key，csco_ajax_load_more為value

# print(data)

res = requests.post(url, headers=headers, data=data)
json_data = res.json()
'''
以下為json_data印出內容：
{'data': {'content': '\n'
                     '\n'
                     '<article class="post-482435 post type-post '
                     'status-publish format-standard has-post-thumbnail '
'''
html_str = json_data["data"]["content"] # 取出html字串(上方為註解說明，先取data，再取content)
soup = BeautifulSoup(html_str, "html.parser")
# pprint.pprint(json_data)
'''
'\t\t\t<h2 class="cs-entry__title"><a '
                     'href="https://www.newmobilelife.com/2023/03/10/steam-sale-230310/">Steam '
                     '知名獨立遊戲《LIMBO》《INSIDE》與眾多商品歷史新低價</a></h2>\n'
                     '\t\t\t\t\t\t\t<div class="cs-entry__excerpt">\n'
'''
for title_obj in soup.select('h2[class="cs-entry__title"]'):
    print(title_obj)
    print("====")