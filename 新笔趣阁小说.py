from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
from tqdm import tqdm


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


# 获取文章章节列表地址和书籍名称
def getListUrl(url):
    content = requestUrl(url)
    dd = content.findAll('dd')
    list = []
    for item in dd:
        list.append('https://www.xbiquge6.com' + item.find('a').get('href'))
    bookName = content.find('dt').text
    list.append(bookName)
    return list


def getContent(list):
    bookName = list[len(list) - 1]
    path = 'E:\%s.txt' % bookName
    for i in tqdm(range(0, len(list))):
        if list[i] != list[len(list) - 1]:
            content = requestUrl(list[i])
            listName = content.find(class_='bookname').find('h1').text
            text = content.find(id='content').text
            with open(path, 'a', encoding='utf-8') as f:
                f.write(listName + '\n')
                f.write(text + '\n')
                f.write('\n')
            # print(listName + '更新完成')


url = input('请输入地址：')
# 获取文章章节列表地址
list = getListUrl(url)
getContent(list)
