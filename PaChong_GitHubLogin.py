"""
from urllib import request
from bs4 import BeautifulSoup
from urllib import parse
# 导入cookie处理模块
from http import cookiejar

# 定义函数返回提交表单数据
def getParams(url, uname, pwd):
    # 请求URL
    req = request.urlopen(url).read().decode('utf-8')
    # 转成Beautifulsoup对象
    obj = BeautifulSoup(req, 'html5lib')
    # 查找表单
    form = obj.find('form')
    # 查找所有的input节点
    listinput = form.find_all('input')
    # 提取name与对应值
    tmp = [[ele.get('name'), ele.get('value')]for ele in listinput]
    params = dict(tmp)
    # 请求参数中添加用户名和密码
    params["login"] = uname
    params["password"] = pwd
    return params

def login(url,params):
    # param进行编码处理
    pdata=parse.urlencode(params,encoding='utf-8')
    # 创建Request对象
    reqhd=request.Request(url=url,data=pdata.encode('utf-8'))
    req=request.urlopen(reqhd)

def setHandler():
    # 创建http和HTTPS处理对象，debug设置为1
    httphd=request.HTTPHandler(debuglevel=1)
    httpshd=request.HTTPSHandler(debuglevel=1)
    # 创建MozillaCookieJar对象，处理cookie
    ckobj=cookiejar.MozillaCookieJar()
    # 创建HTTPCookieProcessor对象
    ckhd=request.HTTPCookieProcessor(ckobj)
    # 创建opener，发起请求后使用http或HTTPS处理请求与应答
    opener=request.build_opener(httphd,httpshd,ckhd)
    # 设置opener
    request.install_opener(opener)

loginurl = 'https://github.com/session'
url = 'https://github.com/login'
# 设置opener
setHandler()
# 请求参数
params = getParams(url, 'zhangsan', '123456')
print('\n')
# 登录
login(loginurl,params)
"""
from urllib import request, parse
from bs4 import BeautifulSoup
from http import cookiejar


class GitHubLogin:
    def __init__(self, loginurl, sessionurl, headers={}):
        # 初始化openner
        self.loginurl = loginurl
        self.sessionurl = sessionurl
        self.hds = headers
        # http/https协议处理对象，打开debug
        httphd = request.HTTPHandler(debuglevel=1)
        httpshd = request.HTTPSHandler(debuglevel=1)
        # cookie处理，引入cookiejar中的MozillaCookieJar类
        # MozillaCookieJar能够保存cookie信息到文件
        self.ckobj = cookiejar.MozillaCookieJar()
        ckhd = request.HTTPCookieProcessor(self.ckobj)
        opener = request.build_opener(httphd, httpshd, ckhd)
        # 安装opener,urllib的每次请求使用opener处理
        request.install_opener(opener)

    def login(self, uname, pwd):
        # 登录接口
        # 请求页面信息
        page = self.requestUrl(self.loginurl)
        # 提取页面信息，获取提交数据
        pdata = self.parsePostData(page, uname, pwd)
        #print(pdata)
        # 提交数据编码处理：utf-8
        pdata = parse.urlencode(pdata).encode('utf-8')
        # 登录
        page=self.requestUrl(self.sessionurl,payload=pdata)
        # 根据返回页面信息与用户名，检查登录是否成功
        return self.loginVerfiy(page,uname)

    def requestUrl(self, url, payload=None):
        # 请求信息，payload=None为GET方法，否则为post方法
        print('reuest url:',url)
        reqhd=request.Request(url,data=payload)
        req=request.urlopen(reqhd)
        if req.code==200:
            content=req.read().decode('utf-8')
            return content

    def parsePostData(self, page, uname, pwd):
        # 提取登录页面信息，返回提交数据
        # 获取input节点，utf8,content,commit,token
        obj=BeautifulSoup(page,'html5lib')
        form=obj.find('form')
        listinput=form.findAll('input')
        result=[[item.get('name'),item.get('value')] for item in listinput]
        result=dict(result)
        # 添加用户名和密码
        result['login']=uname
        result['password']=pwd
        return result

    def loginVerfiy(self, page, uname):
        # 登录验证
        pass

