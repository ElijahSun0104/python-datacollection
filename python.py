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
