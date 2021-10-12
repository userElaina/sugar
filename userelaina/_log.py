import os
import logging

from userelaina._archive import Archive

_log_level={
	'critical':logging.CRITICAL,
	'fatal':logging.FATAL,
	'error':logging.ERROR,
	'warning':logging.WARNING,
	'warn':logging.WARN,
	'info':logging.INFO,
	'debug':logging.DEBUG,
	'all':logging.DEBUG,
}

def fastlog(name:str='Log',level:str='warn',out:str='debug.log',err:str=None,):
		level=level.lower()

		# NOTSET DEBUG INFO WARNING ERROR CRITICAL
		__logger=logging.getLogger(name)
		__logger.setLevel(logging.DEBUG)

		if out:
			Archive().new(out,b=b'----'+name.encode('utf8')+'.'+'DEBUG----')
			handler_lg=logging.FileHandler(filename=out,encoding='utf8')
			handler_lg.setLevel(logging.DEBUG)
			handler_lg.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
			__logger.addHandler(handler_lg)

		if level!='quiet':
			handler_pt=logging.StreamHandler()
			handler_pt.setLevel(_log_level.get(level,logging.WARNING))
			handler_pt.setFormatter(logging.Formatter("%(message)s"))
			__logger.addHandler(handler_pt)

		if err:
			Archive().new(err,b=b'----'+name.encode('utf8')+'.'+'ERROR----')
			handler_er=logging.FileHandler(filename=err,encoding='utf8')
			handler_er.setLevel(logging.ERROR)
			handler_er.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
			__logger.addHandler(handler_er)
		
		return __logger