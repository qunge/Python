# 1. 浏览器中看到信息，抓取数据中提取不到
"""
from urllib import request
from bs4 import BeautifulSoup
# 请求URL
url='https://www.cnblogs.com/aggsite/UserStats/'
# 请求数据，解码
req=request.urlopen(url)
context=req.read().decode('utf-8')
# 创建Beautifulsoup对象
obj=BeautifulSoup(context,'html5lib')
# 查找id=blogger_list元素, 博客排行榜中的作者名称在id=blogger_list的div中
divauthers=obj.find(id='blogger_list').findAll('li')
for val in divauthers:
    if '.' in val.text:
        print(val.text)
"""


# 2. 关键字搜索
"""
我们请求的URL为：https://github.com/search?q=python，请求参数为“q=python”,python为搜索关键字
如果搜索其他内容替换关键字凭借URL即可
"""
"""
from urllib import parse
from urllib import request
# 搜索url
url='https://www.so.com/s?'
# 搜索参数，q对应关键字
kws={'q': '区块链','src': 'srp','fr': 'none','psid': 'd4e99008b6d8326455157cbe204ff5ae'}
# 参数转url
urlkws=parse.urlencode(kws)
# url拼接
url=url+urlkws
req=request.urlopen(url)
print(url)
print(req.code)
"""

# 3. 定制头信息
"""
from urllib import request
import json
url='http://httpbin.org/get'
# 设置请求头信息中的User-Agent
hds={'User-Agent':'Test'}
# 构建Request对象
reqhd=request.Request(url=url,headers=hds)
# 添加头信息
reqhd.add_header('Cookie','uid=test')
reqhd.add_header('Accept-Encoding','gzip,deflate,br')
# 发起请求
req=request.urlopen(reqhd)
content = req.read().decode('utf-8')
"""

# 4. json数据处理
"""
# 转成字典
jdata=json.loads(content)
# 输出类型及对应字段值
print(type(jdata))
print(jdata)
print(jdata.get('headers').get('Host'))
print(jdata.get('url'))
"""

# 5. 发起post请求
# request.Request类中参数data：值为None使用get方法发起请求，否则发起post请求
from urllib import request
from urllib import parse
import json
url='http://httpbin.org/post'
data={'uname':'zhangsan','pwd':'123456'}
# 使用urlencode处理
pdata=parse.urlencode(data).encode('utf-8')
reqhd=request.Request(url,data=pdata)
req=request.urlopen(reqhd)
print(req.read().decode('utf-8'))
