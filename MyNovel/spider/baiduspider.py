# -*-coding=utf-8-*-
'''
发起请求并解析
'''
import urllib2  
from urlparse import urlparse
from function import get_random_user_agent
from config.config import URL_PC, URL_PHONE, LOGGER,  BAIDU_RN
from config.rules import BLACK_DOMAIN, RULES
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def getBaidu(name):
    sheaders = {'user-agent': get_random_user_agent()}
    params = {'wd': name}
    #data = urllib.urlencode(params)  
    url=URL_PC+"?wd="+name
    request = urllib2.Request(url,headers=sheaders)  
    response = urllib2.urlopen(request)  
    page = response.read()  
    soup = BeautifulSoup(page, 'html5lib')
    result = soup.find_all(class_='result')
    extra_tasks=[]
    for i in result:
        item=data_extraction_for_web_baidu( html=i)
        if item != None:
            extra_tasks.append(item)
    return extra_tasks
 
def get_real_url( url):
    headers = {'user-agent': get_random_user_agent()}
    request = urllib2.Request(url,headers=headers)  
    response = urllib2.urlopen(request)  
    url = response.url if response.url else None
    return  url

def getchaperfrompage(url):
    netloc = urlparse(url).netloc
    if netloc not in RULES.keys():
        return None
    content_url = RULES[netloc].content_url
    if content_url==0:
        return None
    content = cache_owllook_novels_chapter(url=url, netloc=netloc)
    if content:
        return {"content":content,"url":url,"content_url":content_url}
    return None

def cache_owllook_novels_chapter(url,netloc):
    sheaders = {'user-agent': get_random_user_agent()}
    request = urllib2.Request(url,headers=sheaders)  
    response = urllib2.urlopen(request)  
    html = response.read()
    
    print html
    soup = BeautifulSoup(html, 'html5lib')
    selector = RULES[netloc].chapter_selector
    if selector.get('id', None):
        content = soup.find_all(id=selector['id'])
    elif selector.get('class', None):
        content = soup.find_all(class_=selector['class'])
    else:
        content = soup.find_all(selector.get('tag'))
    content = str(content).strip('[],')
    return content

def data_extraction_for_web_baidu( html):
            url = html.select('h3.t a')[0].get('href', None)
            real_url = get_real_url(url=url) if url else None
            if real_url:
                netloc = urlparse(real_url).netloc
                if 'baidu' in real_url or netloc in BLACK_DOMAIN:
                    return None
                is_parse = 1 if netloc in RULES.keys() else 0
                if is_parse==0:
                    return None
                title = html.select('h3.t a')[0].get_text()
                return {'title': title, 'url': real_url.replace('index.html', ''), 'is_parse': 1,
                        'netloc': netloc}
            else:
                return None
            
def getContentData(url):
    netloc = urlparse(url).netloc
    if netloc not in RULES.keys():
        return None
    
    sheaders = {'user-agent': get_random_user_agent()}
    request = urllib2.Request(url,headers=sheaders)  
    response = urllib2.urlopen(request)  
    html = response.read()
    
    soup = BeautifulSoup(html, 'html5lib')
    selector = RULES[netloc].content_selector
    if selector.get('id', None):
        content = soup.find_all(id=selector['id'])
    elif selector.get('class', None):
        content = soup.find_all(class_=selector['class'])
    else:
            content = soup.find_all(selector.get('tag'))
    content = str(content).strip('[]Jjs,').replace('http', 'hs')
    return content if content else None

            