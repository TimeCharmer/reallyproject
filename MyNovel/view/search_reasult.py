'''
Created on 2017年4月26日

@author: root
'''
from jinja2 import Environment, PackageLoader, select_autoescape

# jinjia2 config
env = Environment(
    loader=PackageLoader('view.search', '../templates/novels'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']))

def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return template.render(kwargs)

def getResult(uname):
    return template('result.html', title='小年爷的小说搜索引擎', is_login=0)
