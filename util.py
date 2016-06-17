#-*- coding:utf-8 -*-
'''
util.py文本生成器
lines生成器在文件末位加一行空格，标志结束
blocks模块收集所有的行，直到遇见空格
'''
def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block=[]
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block=[]
