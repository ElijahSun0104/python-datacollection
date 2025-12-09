1.1获取网页内容
import request
#用requests库的函数发送请求时，请求头信息不需要手动传入，但是如果将爬虫程序伪装成正常浏览器的话，需要构建一个headers
headers = {"User-Agent": "xxx"……} #怎么看：查看网页源代码-network-刷新一下网页-点击任意请求-展开request headers
request.get("网页完整的url",headers = headers) #print它会返回该网页状态码，如果是200说明请求成功，可以正常访问
#如果要根据状态码进行判断是否成功的话，测试代码如下
response = request.get("网页完整的url")
if response.ok:
  print(response.text) #text属性会以string存储响应内容，因此可以直接获取网页源码
else:
  print("请求失败")
2.1解析html信息
from bs4 import BeautifulSoup
import requests
content = requests.get("网页完整的url").text #将string存储在contenr中
soup = BeautifulSoup(content,"html.parser") #将内容解析成树状结构
all_prices = soup.findAll("p",attrs={"class":"price_color"}) #寻找共性属性
for price in all_prices:
  print(price.string)#可以在string后切片
all_titles = soup.findAll("h3")
for title in all_titles:
  all_links = title.findAll("a")
  for link in all_links:
    print(link.string)
2.2
完整带for循环的代码：
headers = {"User-Agent": "xxx"……}
for start_num in range(0,250，25)：#结束值不包含在范围里
 request.get("网页完整的url{start_num}",headers = headers)
 content = requests.get("网页完整的url").text #将string存储在contenr中
 soup = BeautifulSoup(content,"html.parser") #将内容解析成树状结构
 all_prices = soup.findAll("p",attrs={"class":"price_color"}) #寻找共性属性
 for price in all_prices:
  print(price.string)#可以在string后切片
