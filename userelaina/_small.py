import re
import random
import string

from typing import Union
from time import sleep as slp
from copy import deepcopy as dcp

TEST_INPUT_EOF='/exit_!'

def testinput(f)->None:
    while True:
        a=input('>>> ')
        if a==TEST_INPUT_EOF:
            return
        f(a)

def findargs(x:str)->dict:
    ans=dict()
    for i in re.findall('[\S]+[\s]*=[\s]*[\S]+',x):
        i=re.sub('[\s]+','',i).split('=')
        if i[0] not in ans:
            ans[i[0]]=i[1]
        else:
            ans[i[0]]=[ans[i[0]],i[1]]
    return ans

def newname(n:int)->str:
    try:
        n=max(int(n),1)
    except:
        n=1
    return random.choice(string.ascii_lowercase)+''.join(random.choices(string.digits+string.ascii_lowercase,k=n-1))

def newvname(n:int)->str:
    try:
        n=max(int(n),1)
    except:
        n=1
    return random.choice(string.ascii_lowercase)+''.join(random.choices(string.digits+string.ascii_letters+'_',k=n-1))

def newpwd(n:int,level:int=4)->str:
    try:
        n=max(int(n),6)
    except:
        n=6
    l=(string.digits,string.ascii_lowercase,string.ascii_uppercase,string.punctuation)
    s=''
    ans=list()
    for i in range(level):
        s+=random.choice(l[i])
        ans.append(random.choice(l[i]))
    ans+=random.choices(s,k=max(n-level,0))
    random.shuffle(ans)
    return ''.join(ans)
