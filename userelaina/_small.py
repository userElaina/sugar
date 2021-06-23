import os
import re
import time
import json
import random
from typing import Union

num_type=Union[int,float,str,]
num_types=(int,float,str,)

set_type=Union[list,set,tuple,]
set_types=(list,set,tuple,)

byte_type=Union[bytes,bytearray,memoryview,]
byte_types=(bytes,bytearray,memoryview,)

def pt(x:all)->None:
	print(repr(x))

def rd(x:all)->all:
	return random.choice(list(x))

def trys(s:all,f:type,default=None)->all:
	try:
		return f(s)
	except:
		return default

def teststr(f)->None:
	while True:
		a=input()
		if a.startswith('exit'):
			return
		f(a)

def find_args(x:str)->dict:
	return {
		i[0]:i[1] 
			for i in [re.sub('[\s]+','',j).split('=') 
				for j in re.findall('[\S]+[\s]*=[\s]*[\S]+',x)]
	}

def tot(x:float=None,_=False)->str:
	return time.strftime('%Y-%m-%d %H:%M:%S' if _ else '%Y%m%d%H%M%S',time.localtime(x if x else time.time()))

def lot(l:set_type,indent:Union[int,str]='\n',sort_keys:bool=False)->str:
	if isinstance(int,indent):
		indent=' '*indent
	return str(indent).join([str(i) for i in (sorted(l) if sort_keys else l)])

def jot(
	js:dict,
	indent:Union[int,str]=4,
	ensure_ascii:bool=False,
	sort_keys:bool=False,
)->str:
	ans=json.dumps(js,indent=indent,ensure_ascii=ensure_ascii,skipkeys=True,sort_keys=sort_keys)
	return ans

def sve(x:all,pth:str,sort_keys:bool=True)->None:
	if isinstance(x,dict):
		x=jot(x,sort_keys=sort_keys)
	if isinstance(x,set_types):
		x=lot(x,sort_keys=sort_keys)
	if isinstance(x,byte_types):
		open(pth,'wb').write(x)
	else:
		open(pth,'w',encoding='utf-8',errors='backslashreplace').write(str(x))

def opens(pth:str,default:str='')->str:
	default=''
	try:
		default=open(pth,'r',encoding='utf-8').read()
	except FileNotFoundError:
		open(pth,'w').write(default)
	return default

def openl(pth:str)->list:
	return [i for i in opens(pth).split('\n') if i!='']

def openj(pth:str)->dict:
	return json.loads(opens(pth,'{\n}').read())
