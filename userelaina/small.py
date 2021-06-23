'''
`pt` `rd` `trys` `teststr` `find_args`

`tot` `lot` `jot` `sve`

`opens` `openl` `openj`

`Union` `sh` `rd` `slp` `dcp`

`num` `set` `byte`

	>>> from typing import Union
	>>> from os import system as sh
	>>> from time import sleep as slp
	>>> from copy import deepcopy as dcp

	>>> [num]   int,float,str,
	>>> [set]   list,set,tuple,
	>>> [byte]  bytes,bytearray,memoryview,

	>>> pt(x)->None
	>>> rd(x:all)->all
	>>> trys(s:all,c:type,default=None)->all
	>>> teststr(f:function)->None
	>>> find_args(x:str)->dict

	>>> tot(x:float=None,_=False)->str
	>>> lot(l:set_type,indent='\\n',sort_keys=False)->str
	>>> jot(js:dict,indent=4,ensure_ascii=False,sort_keys=False)->str
	>>> sve(x:all,pth:str,sort_keys=True)
	>>> opens(pth:str,default='')->str
	>>> openl(pth:str)->list
	>>> openj(pth:str)->dict
'''

from userelaina._small import pt,trys,teststr,find_args
from userelaina._small import tot,lot,jot,sve,opens,openl,openj
from userelaina._small import num_type,num_types,set_type,set_types,byte_type,byte_types

from typing import Union
from os import system as sh
from time import sleep as slp
from copy import deepcopy as dcp