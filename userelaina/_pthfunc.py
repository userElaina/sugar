import os
import random
from copy import deepcopy as dcp

class Pth:
	def __init__(
		self,
		old:str='.old',
	):
		self.old=old

	def ck(
		self,
		pth:str,
		l:int=5,
	)->str:
		pth=os.path.abspath(pth)
		if not os.path.exists(pth):
			return
		i=1
		pth2=pth+'.'+str(i).zfill(l)+self.old
		while os.path.exists(pth2):
			i+=1
			pth2=pth+'.'+str(i).zfill(l)+self.old
		os.rename(pth,pth2)
		return pth2

exts={
	'':[''],
	'qwq':['qwq','qwq1','qwq2','qwq3','qwq4','bmp'],
	'pic':['png','jpg','jpeg','gif','bmp','tif','tiff'],
	'tar':['rar','zip','7z','tar','gz','xz','z','bz2'],
	'music':['mp3','wav','flac'],
	'movie':['mp4','mkv','mov','ts'],
	'office':['csv','doc','docx','ppt','pptx','xls','xlsx','pdf'],
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
	'default':'\033[0m',
	'red':'\033[31m',
	'green':'\033[32m',
	'yellow':'\033[33m',
	'blue':'\033[34m',
	'purple':'\033[35m',
	'cyan':'\033[36m',
}
color_name={
	'dft':'default',
	'rd':'red',
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
_s=lambda x:str(x)+(' '*(3-len(str(x))))

class Ls:
	def __init__(
		self,
		pth:str='./',
		l:list=list(),
	):
		self.__pth=os.path.abspath('./')
		self.cd(pth)
		self.__col=dict()
		self.__cols={'red','green','yellow','blue','purple','cyan'}

		for i in l:
			if isinstance(i,str):
				self.paint(i)
			else:
				self.paint(i[0],i[1])

	def __get_col(self)->str:
		ans=random.choice(list(self.__cols))
		if len(self.__cols)>1:
			self.__cols.discard(ans)
		return ans

	def cd(self,pth:str):
		if isinstance(pth,int):
			pth=self.get_clip(pth+2)
		_ans=os.path.abspath(os.path.join(self.__pth,pth))
		self.__pth=_ans if os.path.isdir(_ans) else os.path.dirname(_ans)
		self.__d=['.','..',]
		self.__f=list()
		self.__ext=list()
		for i in os.listdir(self.__pth):
			_full=os.path.join(self.__pth,i)
			if os.path.isdir(_full):
				self.__d.append(i)
			elif os.path.isfile(_full):
				self.__f.append(i)
		self.__up_flg=True

	def paint(self,x:str,y:str=None)->bool:
		if x not in exts:
			return False
		y=color_name[y] if y in color_name else self.__get_col()
		_d={i:y for i in exts[x]}
		self.__col.update(_d)
		self.__up_flg=True
		return True

	def get_pth(self)->str:
		return self.__pth

	def up(self)->dict:
		if not self.__up_flg:
			return dcp(self.__d)
		_col=[self.__col.get(get_ext(i),'default') for i in self.__f]
		_ans=[i for i in self.__f if self.__col.get(get_ext(i),'default')!='default']
		self.__d={
			'pth':self.__pth,
			'dir':self.__d,
			'file':self.__f,
			'ans':_ans,
			'dir_full':[os.path.join(self.__pth,i) for i in self.__d],
			'file_full':[os.path.join(self.__pth,i) for i in self.__f],
			'ans_full':[os.path.join(self.__pth,i) for i in _ans],
			'file_color':_col,
			'ans_color':[i for i in _col if i!='default'],
			'len_dir':len(self.__d)-2,
			'len_file':len(self.__f),
			'len_ans':len(_ans),
		}
		self.__up_flg=False
		return dcp(self.__d)

	def get_clip(self,l:int,r:int=None,k:str='dir')->list:
		_d=self.up()
		if k not in {'dir','file','ans','dir_full','file_full','ans_full'}:
			return list()
		return _d[k][l:r] if r else _d[k][l]

	def showdir(self,fullpath:bool=False,no:bool=False):
		_d=self.up()
		print('dir('+str(_d['len_dir'])+'):')
		_dir=_d['dir_full' if fullpath else 'dir']
		for i in range(_d['len_dir']+2):
			if no:
				print(_s(i-2),end=' ')
			print(os.path.join(_dir[i],''))
		
	def showfile(self,fullpath:bool=False,no:bool=False,onlyans:bool=False,name:str='file'):
		_d=self.up()
		_hd='ans' if onlyans else 'file'
		_file=_d[_hd+('_full' if fullpath else '')]
		print(colors['default']+name+'('+str(_d['len_ans'])+'/'+str(_d['len_file'])+'):')
		for i in range(_d['len_'+_hd]):
			if no:
				print(_s(i),end=' ')
			print(colors[_d[_hd+'_color'][i]]+_file[i]+'\n'+colors['default'],end='')

	def show(self,fullpath:bool=False,no:bool=False):
		print(colors['default'])
		print(colors['green']+self.get_pth()+'# '+colors['default'])
		print(colors['default'])
		self.showdir(fullpath,no)
		print(colors['default'])
		self.showfile(fullpath,no)
		print(colors['default'])