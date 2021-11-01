'''
`testinput` `findargs` `newname` `newvname` `newpwd`

`Union` `slp` `dcp` `TEST_INPUT_EOF`

    >>> from typing import Union
    >>> from time import sleep as slp
    >>> from copy import deepcopy as dcp
    >>> TEST_INPUT_EOF='/exit_!'

    >>> testinput(f:function)->None
    >>> findargs(x:str)->dict
    >>> newname(n:int)->str
    >>> newvname(n:int)->str
    >>> newpwd(n:int,level=4)->str
'''

from userelaina._small import Union,slp,dcp,TEST_INPUT_EOF,testinput,findargs,newname,newvname,newpwd
