import os
from typing import Union
from copy import deepcopy as dcp

from userelaina._small import rd

exts={
	'':[''],
	'archive':['archive'],	
	'qwq':['qwq','qwq1','qwq2','qwq3','qwq4','bmp'],
	'pic':['png','jpg','jpeg','bmp','tif','tiff','gif',],
	'gif':['gif'],
	'tar':['rar','zip','7z','tar','gz','xz','z','bz2'],
	'music':['mp3','wav','flac','ogg'],
	'movie':['mp4','mkv','mov','ts','flv','blv'],
	'blv':['blv'],
	'office':['csv','doc','docx','ppt','pptx','xls','xlsx','pdf','xps'],
	'danger':['vbs','sh','cmd','exe'],
	'html':['html'],
	'txt':['txt','in','out','log'],
	'data':['xml','json','svg','csv','md','rst'],
	'c':['c','cpp','h','hpp'],
	'java':['java'],
	'py':['pyi','py'],
	'othercodes':['cs','go','js','lua','pas','php','r','rb','swift','ts','vb','sh','vbs'],
}
exts['muz']=exts['music']
exts['vid']=exts['movie']
exts['cpp']=exts['c']
exts['python']=exts['py']
exts['codes']=exts['c']+exts['java']+exts['py']+exts['othercodes']+exts['data']
exts['text']=exts['codes']+exts['txt']+exts['html']
def ext(k:str)->list():
	if k.startswith('*.'):
		return [k[2:],]
	return exts.get(k,list())

_white='\x1b[0m'
colors={
	'red':'\x1b[31m',
	'green':'\x1b[32m',
	'yellow':'\x1b[33m',
	'blue':'\x1b[34m',
	'magenta':'\x1b[35m',
	'cyan':'\x1b[36m',
}
def col2str(col:str='default')->str:
	col=str2col(col)
	if col in ('default',0,None,'None'):
		return _white
	if col=='random':
		return rd(colors.values())
	if col in colors:
		return colors[col]
	raise ValueError('Unsupported color!')

color_name={
	'default':['moren','mr','default','dft'],
	'random':['suiji','sj','random','rd'],
	'red':['hong'],
	'green':['lv'],
	'yellow':['huang',],
	'blue':['lan'],
	'magenta':['zi','purple','p','pinhong','ph','fuchsia','yanghong','yh'],
	'cyan':['qing','ding'],
}
for i in colors:
	color_name[i]+=[i,i[0],i[:2]]

def str2col(s:str)->str:
	for i in color_name:
		if s in color_name[i]:
			return i
	return None


def get_ext(s:str)->str:
	_base=os.path.basename(s)
	return _base.rsplit('.',1)[-1].lower() if '.' in _base else ''
fill=lambda s,l:' '*(l-len(str(s)))+str(s)

class Ls:
	def __init__(self,pth:str='./',):
		self.pth='./'
		self.cd(pth)

		self.__n=0
		self.col=dict()
		self.__col_class=dict()
		self.__col_can_use=set(colors)

		self.cho=list()
		self.reg=list()
		self.regtag='None'

	def join(self,pth:str)->str:
		if isinstance(pth,int):
			try:
				pth=self.getreg('dir')[pth]
			except:
				return 1
		else:
			pth=os.path.abspath(os.path.join(self.pth,pth))
		return pth

	def precd(self,pth:str)->str:
		pth=self.join(pth)
		if isinstance(pth,int):
			return 1
		if not os.path.exists(pth):
			return 1
		return pth if os.path.isdir(pth) else os.path.dirname(pth)

	def cd(self,pth:str):
		pth=self.precd(pth)
		if isinstance(pth,int):
			return 1
		if pth==self.pth:
			return 0
		self.pth=pth

		self.dir=list()
		self.file=list()
		for i in os.listdir(self.pth):
			_full=os.path.join(self.pth,i)
			if os.path.isdir(_full):
				self.dir.append(_full)
			elif os.path.isfile(_full):
				self.file.append(_full)
		self.regtag='None'

	def setcolor(self,k:str,y:str=None)->int:
		k=ext(k)
		if not k:
			return 1
		
		y=str2col(y)
		if not y:
			y=self.__n
			self.__n+=1
		for i in k:
			self.col[i]=y
		if len(self.__col_can_use)>1 and y in self.__col_can_use:
			self.__col_can_use.discard(y)
		return 0

	def pwd(self)->str:
		return self.pth

	def explorer(self,pth:str=None):
		x=self.precd(pth)
		os.system('explorer "'+x+'"')
		return x

	def setcho(self,k:str=None,l:int=None,r:int=None)->int:
		self.cho=self.getreg(k,l,r)
		return len(self.cho)

	def addcho(self,k:str=None,l:int=None,r:int=None)->int:
		if isinstance(k,(list,set,tuple)):
			_l=list(k)
		else:
			_l=self.getreg(k,l,r)
		_l=[i for i in _l if i not in self.cho]
		self.cho+=_l
		if self.regtag=='chosen' and _l:
			self.regtag='None'
		return len(_l)

	def uncho(self,k:str=None,l:int=None,r:int=None)->int:
		if isinstance(k,(list,set,tuple)):
			_l=list(k)
		else:
			self.getreg('chosen')
			_l=self.getreg(k,l,r)
		self.cho=[i for i in self.cho if i not in _l]
		if self.regtag=='chosen' and _l:
			self.regtag='None'
		return len(_l)
	
	def delcho(self,k:str=None)->int:
		if k is None:
			_d=len(self.cho)
			self.cho=list()
		else:
			_d=0
			while k in self.cho:
				_d+=1
				self.cho.remove(k)
		if self.regtag=='chosen' and _d:
			self.regtag='None'
		return _d

	def lencho(self)->int:
		return len(self.cho)

	def getcho(self,l:int=None,r:int=None)->Union[str,list]:
		return self.getreg('chosen',l,r)

	def findcho(self,x:str)->int:
		try:
			return self.cho.index(x)
		except:
			return -1

	def setreg(self,k:str='file')->int:
		if k is None or k==self.regtag:
			return len(self.reg)

		if k=='dir':
			self.reg=dcp(self.dir)

		elif k=='file':
			self.reg=dcp(self.file)
		elif k=='ans':
			self.reg=[i for i in self.file if get_ext(i) in self.col]
		elif k=='chosen':
			self.reg=dcp(self.cho)
		elif k in exts:
			self.reg=[i for i in self.file if get_ext(i) in exts[k]]
		elif k.startswith('*.'):
			k=k[2:]
			self.reg=[i for i in self.file if get_ext(i)==k]
		else:
			return len(self.reg)
		self.regtag=k
		return len(self.reg)

	def fxxkreg(self,reg:list,regtag:str):
		'WARNING: This is a dangerous behavior!'
		if reg is not None:
			self.reg=reg
		self.regtag=regtag

	def getreg(self,k:str=None,l:int=None,r:int=None)->Union[str,list]:
		if isinstance(k,int):
			k,l,r=None,k,l
		self.setreg(k)
		if l is None:
			if r is None:
				return dcp(self.reg)
			else:
				try:
					return self.reg[r]
				except:
					return None
		else:
			if r is None:
				try:
					return self.reg[l]
				except:
					return None
			else:
				return self.reg[l:r]
		return dcp(self.reg)
	
	def getregtag(self):
		return self.regtag

	def showreg(self,k:str='file',fullpath:bool=False,num:bool=True)->str:
		_d=self.getreg(k)
		_filllen=max(len(str(len(_d))),2 if k=='dir' else 1)
		s=col2str()+k+'('+str(len(_d))
		if k in exts or k.startswith('*.') or k in ('ans'):
			s+='/'+str(len(self.file))
		s+='):\n'

		if k=='dir':
			s+=(fill(-2,_filllen)+' ') if num else ''
			p=os.path.join('..','')
			s+=os.path.join(self.pth,p) if fullpath else p
			s+='\n'

			s+=(fill(-1,_filllen)+' ') if num else ''
			p=os.path.join('.','')
			s+=os.path.join(self.pth,p) if fullpath else p
			s+='\n'

			for i in enumerate(_d):
				s+=(fill(i[0],_filllen)+' ') if num else ''
				s+=os.path.join(i[1] if fullpath else os.path.basename(i[1]),'')
				s+='\n'
			s+=col2str()
			return s

		s+=col2str()
		_cc=dict()
		_ca=list(self.__col_can_use)
		for i in enumerate(_d):
			s+=(fill(i[0],_filllen)+' ') if num else ''

			_c=self.col.get(get_ext(i[1]),'default')
			if isinstance(_c,int):
				if _c not in _cc:
					_cc[_c]=rd(_ca)
					if len(_ca)>1:
						_ca.remove(_cc[_c])
				_c=_cc[_c]

			s+=col2str(_c)
			s+=i[1] if fullpath else os.path.basename(i[1])
			s+='\n'+col2str()
		return s

	def show(self,fullpath:bool=False,num:bool=True):
		print(col2str())
		print(col2str('green')+self.pth+'# ')
		print(col2str())
		print(self.showreg(k='dir',fullpath=fullpath,num=num))
		print(self.showreg(k='file',fullpath=fullpath,num=num))
