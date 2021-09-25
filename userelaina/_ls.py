import os
from typing import Union
from copy import deepcopy as dcp

from userelaina._small import rd

exts={
	'':[''],
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

colors={
	'red':'\x1b[31m',
	'green':'\x1b[32m',
	'yellow':'\x1b[33m',
	'blue':'\x1b[34m',
	'purple':'\x1b[35m',
	'cyan':'\x1b[36m',
}
def col2str(col:str='default')->str:
	if col in ('default',0,None,'None'):
		return '\x1b[0m'
	if col=='random':
		return rd(colors.values())
	if col in colors:
		return colors[col]
	raise ValueError('Unsupported color!')

color_name={
	'default':'default',
	'random':'random',

	'suiji':'random',
	'sj':'random',
	'moren':'default',
	'mr':'default',
	'hong':'red',
	'lv':'green',
	'huang':'yellow',
	'lan':'blue',
	'zi':'putple',
	'qing':'cyan',

	'dft':'default',
	'yl':'yellow',
	'pp':'purple',
	'ppl':'purple'
}
for i in colors:
	color_name[i]=i
	color_name[i[0]]=i
	color_name[i[:2]]=i

def get_ext(s:str)->str:
	_base=os.path.basename(s)
	return _base.rsplit('.',1)[-1].lower() if '.' in _base else ''
fill=lambda s,l:' '*(l-len(str(s)))+str(s)

class Ls:
	def __init__(
		self,
		pth:str='./',
		l:list=list(),
	):
		self.pth=os.path.abspath('./')
		self.cd(pth)
		_paint=dict()
		self.__col_class=dict()
		self.__col_can_use=set(colors)
		self.chosen=list()
		self.reg=list()

		for i in l:
			if isinstance(i,str):
				self.paint(i)
			else:
				self.paint(i[0],i[1])

	def cd(self,pth:str):
		if isinstance(pth,int):
			pth=self.get_clip(pth+2)
		_ans=os.path.abspath(os.path.join(self.pth,pth))
		self.pth=_ans if os.path.isdir(_ans) else os.path.dirname(_ans)
		self.dir=list()
		self.file=list()
		for i in os.listdir(self.pth):
			_full=os.path.join(self.pth,i)
			if os.path.isdir(_full):
				self.dir.append(i)
			elif os.path.isfile(_full):
				self.file.append(i)

	def setcolor(self,x:str,y:str=None)->int:
		if x not in exts:
			return 1
		self.__col_class[x]=color_name.get(y,'random')
		if len(self.__col_can_use)>1:
			self.__col_can_use.discard(y)
		return 0

	def pwd(self)->str:
		return self.pth

	def explorer(self):
		return os.system('explorer "'+self.pth+'"')

	def setreg(self,k:str='file'):
		if k is None:
			return self.reg

		_paint=dict()
		for i in self.__col_class:
			co=rd(self.__col_can_use) if self.__col_class[i]=='random' else self.__col_class[i]
			if i.startswith('.'):
				_paint[i[1:]]=co
			_paint.update({j:co for j in exts[i]})

		if k=='dir':
			self.reg=[(i,'default') for i in self.dir]

		if k=='file':
			self.reg=[(i,_paint.get(get_ext(i),'default')) for i in self.file]
		if k=='ans':
			self.reg=[(i,_paint.get(get_ext(i),'default')) for i in self.file if get_ext(i) in _paint]
		if k in exts:
			self.reg=[(i,_paint.get(get_ext(i),'default')) for i in self.file if get_ext(i) in exts[k]]
		if k.startswith('.'):
			k=k[1:]
			_c=_paint.get(k,'default')
			self.reg=[(i,_c) for i in self.file if get_ext(i)==k]
		return self.reg

	def getreg(self,k:str=None,l:int=None,r:int=None)->Union[str,list]:
		_d=[os.path.join(self.pth,i[0]) for i in self.setreg(k)]
		if l==None and r==None:
			return _d[k]
		if l==None:
			return _d[k][r]
		if r==None:
			return _d[k][l]
		return _d[k][l:r]

	def showreg(self,k:str='file',fullpath:bool=False,num:bool=True)->str:
		_d=self.setreg(k)
		_filllen=max(len(str(len(_d))),2 if k=='dir' else 1)
		s=col2str()+k+'('+str(len(_d))
		if k not in ('file','dir'):
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
				p=os.path.join(i[1][0],'')
				s+=os.path.join(self.pth,p) if fullpath else p
				s+='\n'
			s+=col2str()
			return s

		s+=col2str()
		for i in enumerate(_d):
			s+=(fill(i[0],_filllen)+' ') if num else ''
			s+=col2str(i[1][1])
			s+=os.path.join(self.pth,i[1][0]) if fullpath else i[1][0]
			s+='\n'+col2str()
		return s

	def show(self,fullpath:bool=False,num:bool=True):
		print(col2str())
		print(colors['green']+self.pth+'# ')
		print(col2str())
		print(self.showreg(k='dir',fullpath=fullpath,num=num))
		print(self.showreg(fullpath=fullpath,num=num))
		print(col2str())

