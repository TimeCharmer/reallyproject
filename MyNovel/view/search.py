#coding=utf-8
'''
Created on 2017年4月26日

@author: root

反馈模板
'''

from jinja2 import Environment, PackageLoader, select_autoescape
import spider.baiduspider as bd
import re
# jinjia2 config
env = Environment(
    loader=PackageLoader('view.search', '../templates/novels'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']))

def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return template.render(kwargs)

def getSearchPage():
    return template('index.html', title='小年爷的小说搜索引擎', is_login=0)

def getError():
     return template('../except/404.html', title='Error', is_login=0)

def getChapter(url):
    content=bd.getchaperfrompage(url)
    if content:
        #return content.decode('unicode_escape')
        if content['content_url']=='1':
            soap= content['content'].replace("href=\"", "href=\"/content?url=").decode('unicode_escape')
        elif content['content_url']=='0':
            soap= content['content'].replace("href=\"", "href=\"/content?url="+content['url']).decode('unicode_escape')
        else:
            soap= content['content'].replace("href=\"", "href=\"/content?url="+content['content_url']).decode('unicode_escape')
        return template('chapter.html',soap=soap,url=content['url'])
    else:
        return "解析失败"
    
def getContent(url):
    content=bd.getContentData(url).decode('unicode_escape')
    return template('content.html',url=url,content=content)

def getResult(uname):
    list=bd.getBaidu(uname)
    return template('result.html',name=uname,result=list)
