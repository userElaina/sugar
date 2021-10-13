import re
import random

def pt(x:all)->None:
    print(repr(x))

def rd(x:all)->all:
    return random.choice(list(x))

def teststr(f)->None:
    while True:
        a=input('>>> ')
        if a=='exit!!!':
            return
        f(a)

def find_args(x:str)->dict:
    return {
        i[0]:i[1]
            for j in re.findall('[\S]+[\s]*=[\s]*[\S]+',x)
                for i in re.sub('[\s]+','',j).split('=')
    }
