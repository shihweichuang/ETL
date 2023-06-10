from urllib import request

url = 'http://httpbin.org/get' #宣告一字串

res = request.urlopen(url = url)

print(res) #印出一物件<http.client.HTTPResponse object at 0x000001B874E45D00>


html = res.read() #先宣告一變數，接住res.read()

print(html)

# print(res.read()) #直接列印res.read()
# print(res.read()) #如果已經讀過一次，第二次就不會跑出內容

# print(html.decode('utf-8')) #decode進行解碼，印出一json
print(type(res.read().decode('utf-8'))) #印出 <class 'str'> 型態為字串