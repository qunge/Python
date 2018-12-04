from urllib import request
from bs4 import BeautifulSoup


# 定义函数返回提交表单数据
def getParams(url, uname, pwd):
    # 请求URL
    req = request.urlopen(url).read().decode('utf-8')
    # 转成Beautifulsoup对象
    obj = BeautifulSoup(req, 'html5lib')
    # 查找表单
    form=obj.find('form')
    # 查找所有的input节点
    listinput=form.find_all('input')
    # 提取name与对应值
    

url = 'https://github.com/login'
getParams(url, 'zhangsan', '123456')
