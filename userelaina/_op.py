import os
import json
import string
from typing import Union

from userelaina._archive import Archive
from copy import deepcopy as dcp

_Default=__name__+'._Default'

def _l_indent(indent:str)->str:
	if indent==_Default:
		return '\n'
	if not indent:
		return ''
	if isinstance(indent,int):
		return ' '*indent
	return str(indent)


class Op:
	def __init__(self):
		None

	def enc(
		x:all,
		indent:Union[None,int,str]=_Default,
		ensure_ascii:bool=False,
		sort_keys:bool=False,
	)->bytes:
		if isinstance(x,dict):
			x=json.dumps(
				x,
				indent=4 if indent==_Default else indent,
				ensure_ascii=ensure_ascii,
				skipkeys=True,
				sort_keys=sort_keys,
			)
		if isinstance(x,(list,set,tuple,)):
			x=_l_indent(indent).join([
				str(i) for i in (sorted(x) if sort_keys else x)
			])
		if isinstance(x,(bytes,bytearray,memoryview,)):
			x=bytes(x)
		else:
			x=str(x).encode(
				encoding='unicode_escape' if ensure_ascii else 'utf-8',
				errors='backslashreplace',
			)
		return x

	def w(
		x:all,
		pth:str,
		indent:Union[None,int,str]=_Default,
		ensure_ascii:bool=False,
		sort_keys:bool=False,
		save_old:bool=False,
	)->None:
		x=Op.enc(
			x,
			indent=indent,
			ensure_ascii=ensure_ascii,
			sort_keys=sort_keys,
		)
		if save_old:
			Archive().new(pth,x)
		return x

	def dec(
		x:bytes,
		t:type=bytes,
		indent:Union[None,int,str]='\n',
		ensure_ascii:bool=False,
		lfunc=str,
	)->all:
		if t==bytes:
			if isinstance(x,(bytes,bytearray,memoryview,)):
				return bytes(x)
			return str(x).encode(
				encoding='utf-8',
				errors='backslashreplace',
			)

		if t==dict:
			return json.loads(x)

		if isinstance(x,(bytes,bytearray,memoryview,)):
			x=bytes(x).decode(
				encoding='unicode_escape' if ensure_ascii else 'utf-8',
				errors='backslashreplace',
			)
		x=str(x)

		if t==str:
			return x
		if t in [list,set,tuple]:
			x=[lfunc(i) for i in x.split(_l_indent(indent)) if i!='']
		try:
			return t(x)
		except:
			return None

	def r(
		pth:str,
		t:type=bytes,
		indent:Union[None,int,str]='\n',
		ensure_ascii:bool=False,
		lfunc=str,
		default:bytes=_Default,
		w:bool=True,
	)->all:
		if os.path.exists(pth):
			default=open(pth,'rb').read()
		else:
			if default==_Default:
				if t in [str,bytes,bool,list,tuple,set]:
					default=b''
				if t==dict:
					default=b'{}'
				if t in [int,float]:
					default=b'0'
			default=Op.enc(default)
			if w:
				open(pth,'wb').write(default)
		return Op.dec(
			default,
			t=t,
			indent=indent,
			ensure_ascii=ensure_ascii,
			lfunc=lfunc,
		)

	def denc(
		x:all,
		pth:str,
		xisnew:bool=False,
		indent:Union[None,int,str]='\n',
		ensure_ascii:bool=False,
		lfunc=str,
		w:bool=True,
	)->all:
		if isinstance(x,tuple):
			x=list(x)
		if isinstance(x,(bytearray,memoryview,)):
			x=bytes(x)
		if not isinstance(x,(str,bytes,int,float,list,set,dict)):
			x=str(x)
		t=type(x)

		y=Op.r(
			pth,
			t=t,
			indent=indent,
			ensure_ascii=ensure_ascii,
			lfunc=lfunc,
			w=w,
		)
		if y==None:
			raise RuntimeError(__name__+'.'+Op.__class__.__name__+': Cannot load "'+pth+'"!')
		
		if t==set:
			return x|y
		if t in (int,float):
			return x+y

		
		if xisnew:
			x,y=y,x
		
		if t in (str,bytes,list,):
			return x+y
		if t==dict:
			ans=dcp(x)
			ans.update(y)
			return dcp(ans)
		
		raise RuntimeError('WFT')
	
	def a(
		x:all,
		pth:str,
		xisnew:bool=True,
		indent:Union[None,int,str]=_Default,
		ensure_ascii:bool=False,
		lfunc=str,
		sort_keys:bool=False,
		save_old:bool=True,
	)->None:
		x=Op.denc(
			x,
			pth,
			xisnew=xisnew,
			indent=indent,
			ensure_ascii=ensure_ascii,
			lfunc=lfunc,
			w=save_old,
		)
		Op.w(
			x,
			pth,
			indent=indent,
			ensure_ascii=ensure_ascii,
			sort_keys=sort_keys,
			save_old=save_old,
		)
		return x
