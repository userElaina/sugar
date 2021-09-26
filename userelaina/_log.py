import os
import logging

from userelaina._archive import Archive

class Log:
	def __init__(
		self,
		out:str='debug.log',
		err:str=None,
		name:str='Log',
	):
		# NOTSET DEBUG INFO WARNING ERROR CRITICAL
		self.__logger=logging.getLogger(name)
		self.__logger.setLevel(logging.DEBUG)

		if out:
			self.out=os.path.abspath(out)
			Archive().new(self.out)
			handler_lg=logging.FileHandler(filename=self.out,encoding='utf-8')
			handler_lg.setLevel(logging.DEBUG)
			handler_lg.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
			self.__logger.addHandler(handler_lg)

		handler_pt=logging.StreamHandler()
		handler_pt.setLevel(logging.INFO)
		handler_pt.setFormatter(logging.Formatter("%(message)s"))
		self.__logger.addHandler(handler_pt)

		if err:
			self.err=os.path.abspath(err)
			Archive().new(self.err)
			handler_er=logging.FileHandler(filename=self.err,encoding='utf-8')
			handler_er.setLevel(logging.ERROR)
			handler_er.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
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

