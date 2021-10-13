'''
`Op` `Archive` `Ls`

`col2str` `fastlog`

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

    >>> Archive(base=10,le=3,lstr='.',rstr='.archive',table:str)
    >>> Ls(pth='./')

    >>> col2str(col='default')->str
    >>> fastlog(name='Log',level='warn',out='debug.log',err:str)->logger
'''

from userelaina._op import Op
from userelaina._archive import Archive
from userelaina._ls import exts,col2str,Ls
from userelaina._log import fastlog
