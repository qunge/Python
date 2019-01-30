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
    # 获取页面内容
    content = requestUrl(url)
    # 获取文章所有的章节地址
    dd = content.findAll('dd')
    list = []
    # 将所有的章节地址添加到列表中
    for item in dd:
        list.append('https://www.xbiquge6.com' + item.find('a').get('href'))
    # 获取书籍名称
    bookName = content.find('dt').text
    # 将书籍名称添加到列表中
    list.append(bookName)
    # 返回列表
    return list


# 保存文章
def getContent(list):
    # 获取书籍名称
    bookName = list[len(list) - 1]
    # 文章保存路径
    path = 'E:\%s.txt' % bookName
    # 遍历章节地址列表的信息并增加进度条（tqdm为进度条库）
    for i in tqdm(range(0, len(list))):
        # 判断该条信息是否为文章名称
        if list[i] != list[len(list) - 1]:
            # 请求文章内容
            content = requestUrl(list[i])
            # 获取章节名称
            listName = content.find(class_='bookname').find('h1').text
            # 获取章节内容
            text = content.find(id='content').text
            # 保存文章
            with open(path, 'a', encoding='utf-8') as f:
                f.write(listName + '\n')
                f.write(text + '\n')
                f.write('\n')
            # print(listName + '更新完成')


# 输入文章列表页地址
url = input('请输入文章列表页地址：')
# 获取文章章节列表地址
list = getListUrl(url)
getContent(list)
