import requests
import pprint
import os

folder_path = "./photo"
if not os.path.exists(folder_path):   # 建立資料夾
    os.mkdir(folder_path)

url = "https://www.nownews.com/nn-client/api/v1/cat/column/?pid=6085665"

headers = {
    "user-Ageng": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"
}

res = requests.get(url, headers=headers)

# print(res.text)

# json_data = json.loads(res.text)
# pprint.pprint(json_data)

# pprint.pprint(res.json()) # 效果同上

for article_obj in res.json()["data"]["newsList"]:
    post_title = article_obj["postTitle"] # 取出posttitle
    post_url = "https://www.nownews.com" + article_obj["postUrl"]
    image_url = article_obj["imageUrl"]
    image_concent = requests.get(image_url, headers=headers).content # 圖片二進式內容
    image_type = image_url.split('.')[-1].split('?')[0].replace('/','-') # 照片名稱，因較長故獨立成一變數
    image_path = f"{folder_path}/{post_title}.{image_type}" # 照片儲存位置

    with open(image_path, "wb") as f: # 照片儲存成二進制
        f.write(image_concent)

    print(post_title)
    print(post_url)
    print(image_url)
    print(image_path)
    print("======")