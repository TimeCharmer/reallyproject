# coding=utf-8
'''
Created on 2017年4月20日

@author: root
启动服务与路由匹配
'''
from bottle import route, run, template, get, post, request,error
from view import search

import sys
reload(sys)
sys.setdefaultencoding('utf8')

@route('/static/img/<filename>')
def server_img_static(filename):
    filename +=".png"
    return static_file(filename, root='/') 

@route('/search')
@get('/search')
def getfrombaidu():
    uname = request.GET.get('wd')
    return search.getResult(uname)

@error(404)
def error404(error):
    return search.getError()

@route('/')
def index():
    return search.getSearchPage()

@route('/content')
@get('/content')
def content():
    url = request.GET.get('url',None)
    return search.getContent(url)

@route('/chapter')
@get('/chapter')
def chapter():
    url = request.GET.get('url',None)
    return search.getChapter(url)
run(host='0.0.0.0', port=10079)
