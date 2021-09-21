'''
`Op` `Old` `Ls` `Log`

	>>> Op.enc(
			x:all,
			indent=_Default,
			ensure_ascii=False,
			sort_keys=False,
		)->bytes
	>>> Op.w(
			x:all,
			pth:str,
			indent:Union=_Default,
			ensure_ascii=False,
			sort_keys=False,
			save_old=False,
		)->None
	>>> Op.dec(
			x:bytes,
			t=bytes,
			indent='\\n',
			ensure_ascii=False,
		)->all
	>>> Op.r(
			pth:str,
			t=bytes,
			indent='\\n',
			ensure_ascii=False,
			default=_Default,
			w=True,
		)->all
	>>> Op.denc(
			x:all,
			pth:str,
			xisnew=False,
			indent='\n',
			ensure_ascii=False,
			w=True,
		)->all
	>>> Op.a(
			x:all,
			pth:str,
			xisnew=True,
			indent=_Default,
			ensure_ascii=False,
			sort_keys=False,
			save_old=False,
		)->None

	>>> Old(base=10,le=3,lstr='.',rstr='.achieve',table:str)
	>>> Ls(pth='./',l=list())
	>>> Log(pth='debug.log',erpth='error.log')
'''

from userelaina._op import Op
from userelaina._old import Old
from userelaina._ls import exts,Ls
from userelaina._log import Log
