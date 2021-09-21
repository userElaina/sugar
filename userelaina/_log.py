import os
import logging

from userelaina._old import Old

class Log:
	def __init__(
		self,
		pth:str='debug.log',
		err:str='error.log',
	):
		# DEBUG INFO WARNING ERROR CRITICAL
		self.__logger=logging.getLogger('Log')
		self.__logger.setLevel(logging.DEBUG)
		formatter=logging.Formatter("%(asctime)s %(message)s")

		if pth:
			self.__pth=os.path.abspath(pth)
			Old().ck(self.__pth)
			open(self.__pth,'wb')
			handler_lg=logging.FileHandler(filename=self.__pth,encoding='utf-8')
			handler_lg.setLevel(logging.DEBUG)
			handler_lg.setFormatter(formatter)
			self.__logger.addHandler(handler_lg)

		handler_pt=logging.StreamHandler()
		handler_pt.setLevel(logging.INFO)
		handler_pt.setFormatter(logging.Formatter("%(message)s"))
		self.__logger.addHandler(handler_pt)

		if err:
			self.__err=os.path.abspath(err)
			s=Old().ck(self.__pth,True)
			open(self.__err,'wb')
			handler_er=logging.FileHandler(filename=self.__err,encoding='utf-8')
			handler_er.setLevel(logging.ERROR)
			handler_er.setFormatter(formatter)
			self.__logger.addHandler(handler_er)

	def lg(self,s:str):
		s=str(s)
		self.__logger.debug(s)

	def pt(self,s:str):
		s=str(s)
		self.__logger.info(s)

	def er(self,s:str):
		s=str(s)
		self.__logger.error(s)

	def ptr(self,s:all):
		pt(repr(s))
