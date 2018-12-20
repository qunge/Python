# 1. 浏览器中看到信息，抓取数据中提取不到
from urllib import request
from bs4 import BeautifulSoup
# 请求URL
url='https://www.cnblogs.com/'
# 请求数据，解码
req=request.urlopen(url)
context=req.read().decode('utf-8')
# 创建Beautifulsoup对象
obj=BeautifulSoup(context,'html5lib')
