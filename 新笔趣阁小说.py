from urllib import request
from urllib import parse
from bs4 import BeautifulSoup

# 页面请求
def requestUrl(url):
    # 定义请求头信息
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    # # 对输入的关键字做字典处理
    # wd = {'keyword': keyWorld}
    # wd = parse.urlencode(wd)
    # # 拼接完整的url
    # fullUrl = url + wd
    # 构建请求对象
    rt = request.Request(url, headers=header)
    # 请求网页获取响应
    response = request.urlopen(rt)
    respon = response.read()
    content = BeautifulSoup(respon, 'html5lib')
    return content


# 获取文章章节列表地址
def getListUrl(url):
    content=requestUrl(url)
    dd=content.findAll('dd')
    list=[]
    for item in dd:
        list.append('https://www.xbiquge6.com'+item.find('a').get('href'))
    return list

def getContent(list):
    for i in list:
        content = requestUrl(i)
        bookName = content.find(class_='bookname').find('h1').text
        text=content.find(id='content').text
        path='E:\恶明.txt'
        f=open(path,'a',encoding='utf-8')
        f.write(bookName+'\n')
        f.write(text+'\n')
        f.write('\n')
        f.close()
        print(bookName+'更新完成')

url=input('请输入地址：')
# 获取文章章节列表地址
list = getListUrl(url)
getContent(list)