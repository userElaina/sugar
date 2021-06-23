import os
import logging
from userelaina._pthfunc import Pth

class Log:
	def __init__(
		self,
		pth:str='py.log',
		erpth:str=None,
	):
		bg=list()

		
		self.__pth=os.path.abspath(pth)
		s=Pth('.log').ck(self.__pth)
		open(self.__pth,'wb')
		if s:
			bg.append(self.__pth+' already exists, and then it is moved '+s)

		if erpth:
			self.__err=os.path.abspath(erpth)
			s=Pth('.log').ck(self.__err)
			open(self.__err,'wb')
			if s:
				bg.append(self.__err+' already exists, and then it is moved '+s)

		bg.append('Log start!')
		
		'DEBUG INFO WARNING ERROR CRITICAL'
		self.__logger=logging.getLogger('Log')
		self.__logger.setLevel(logging.DEBUG)
		formatter=logging.Formatter("%(asctime)s %(message)s")

		handler_lg=logging.FileHandler(filename=self.__pth,encoding='utf-8')
		handler_lg.setLevel(logging.DEBUG)
		handler_lg.setFormatter(formatter)
		self.__logger.addHandler(handler_lg)

		handler_pt=logging.StreamHandler()
		handler_pt.setLevel(logging.INFO)
		handler_pt.setFormatter(logging.Formatter("%(message)s"))
		self.__logger.addHandler(handler_pt)

		if erpth:
			handler_er=logging.FileHandler(filename=self.__err,encoding='utf-8')
			handler_er.setLevel(logging.ERROR)
			handler_er.setFormatter(formatter)
			self.__logger.addHandler(handler_er)

		for i in bg:
			self.er(i)

	def lg(self,s:str):
		s=str(s)
		self.__logger.debug(s)

	def pt(self,s:str):
		s=str(s)
		self.__logger.info(s)

	def er(self,s:str):
		s=str(s)
		self.__logger.error(s)

	def ptr(self,s:str):
		pt(repr(s))
