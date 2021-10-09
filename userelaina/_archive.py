import os
import string

SAFE_B64_AB=string.digits+string.ascii_letters+'+-='

class Archive:
	def __init__(
		self,
		base:int=10,
		le:int=3,
		lstr:str='.',
		rstr:str='.archive',
		table:str=SAFE_B64_AB,
	):
		self.setle(le)
		self.setbase(base)
		self.setstr(lstr,rstr)
		self.settable(table)

		self.ck=self.check
		self.save=self.check
		self.sv=self.check
		self.mv=self.move
		self.preopen=self.new

	def setbase(self,base:int):
		try:
			base(233)+''
			self.mx=base(-1)
			self.func=lambda x:str(base(x))
		except:
			try:
				base=abs(int(base))
			except:
				base=10
			if base<2:
				base=10
			self.mx=base**self.le
			self.func=lambda x:self.t(x,base)
		self.base=base

	def setle(self,le:int)->None:
		self.le=le

	def setstr(self,lstr:str,rstr:str)->None:
		self.setlstr(lstr)
		self.setrstr(rstr)

	def setlstr(self,lstr:str)->None:
		self.l=lstr
	
	def setrstr(self,rstr:str)->None:
		self.r=rstr

	def settable(self,table:str)->None:
		self.table=table

	def t(self,x:int,k:int)->str:
		if x==0:
			return '0'
		b=''
		while x!=0:
			b=self.table[x%k]+b
			x=x//k
		return b

	def __save_old(self,pth:str,)->str:
		if not os.path.exists(pth):
			return 0
		for i in range(self.mx):
			pth2=pth+self.l+self.func(i)+self.r
			if not os.path.exists(pth2):
				os.rename(pth,pth2)
				return pth2
		return -1

	def mkdir(self,pth:str)->int:
		pth=os.path.abspath(pth)
		if os.path.exists(pth):
			return 1
		os.makedirs(pth,exist_ok=True)
		return 0

	def check(self,pth:str,save_old:bool=True)->int:
		pth=os.path.abspath(pth)
		ans=self.mkdir(os.path.dirname(pth))
		if save_old:
			s=self.__save_old(pth)
			if s==1:
				raise RuntimeError(__name__+'.'+self.__class__.__name__+': Too many "'+pth+'"s!')
		return ans
	
	def new(self,pth:str,save_old:bool=True,b:bytes=b'')->int:
		self.check(pth,save_old=save_old)
		open(pth,'wb').write(b)

	def move(self,src:str,dst:str,save_old:bool=True)->int:
		src=os.path.abspath(src)
		if not os.path.exists(src):
			return 1
		self.check(dst,save_old=save_old)
		os.rename(src,dst)
		return 0

