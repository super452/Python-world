#encoding: UTF-8
import urllib.request
import re
#建立函数读取网页代码
def gethtml(url):
    response_html = urllib.request.urlopen(url)
    html = response_html.read()
    html = html.decode('UTF-8')
    return html
#匹配网页代码
def geturl(html):
    reg = r'blank">\r''(.+?)''\n'  #建立匹配规则
    html_a = re.compile(reg)  #编译成正则对象
    urllist = re.findall(html_a,html)
    return urllist
html = gethtml('url')  #url即网址
print (geturl(html))
