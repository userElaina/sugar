import os
import time
import threading

def getlock():
    return threading.Lock()

_lk=getlock()

def lock(x=None,un:bool=False):
    if x is None:
        x=_lk
    return x.release() if un else x.acquire()

def unlock(x=None):
    if x is None:
        x=_lk
    return x.release()

def throws(f,args:tuple=tuple())->None:
    if not f:
        f=args

    if isinstance(f,(list,tuple)):
        if len(f)==1:
            args=tuple()
        elif len(f)==2:
            args=f[1]
        else:
            args=f[1:]
        f=f[0]

    if not isinstance(args,tuple):
        args=(args,)
    _t=threading.Thread(target=f,args=args,daemon=True)
    _t.start()
    return _t

class nThread:
    def __init__(
        self,
        f:callable,
        n:int=None,
        clk:float=0,
        name:str='nThread',
    ):
        self.__kill=False
        self.__end=False
        self.__pause=False
        self.__q=list()

        try:
            n=int(n)
            if n<0:
                raise ValueError
        except:
            n=os.cpu_count()
        self.__n=n
        self.__total=0
        self.__finish=0

        self.__f=f
        self.clk=clk
        self.name=name

    def __iter__(self):
        for i in self.__q.copy():
            yield i

    def __str__(self):
        return '<%s with %d threads>'%(self.name,self.__n)

    def __always(self):
        _l=list()
        while True:
            time.sleep(self.clk)

            if self.__kill:
                return
            if self.__end and not len(_l):
                return
            if self.__pause:
                continue

            for i in _l.copy():
                if not i.is_alive():
                    _l.remove(i)
                    self.__finish+=1
            while self.__q and len(_l)<self.__n:
                _l.append(throws(self.__f,self.__q.pop(0)))

    def get_queue(self)->list:
        return self.__q.copy()

    def get_info(self)->dict:
        _total=self.__total
        _finish=self.__finish
        _wait=len(self.__q)
        _d={
            'name':self.name,
            'clock':self.clk,
            'threads':self.__n,
            'running':_total-_finish-_wait,
            'total':_total,
            'finished':_finish,
            'waiting':_wait,
        }
        return _d

    def append(self,args:tuple=tuple()):
        self.__total+=1
        self.__q.append(args)

    def add(self,l:list):
        _total=self.__total
        if isinstance(l,int):
            l=list(range(_total,_total+l))
        self.__total+=len(l)
        self.__q+=l

    def pause(self):
        self.__pause=~self.__pause

    def autoexit(self):
        self.__end=True

    def exit(self):
        self.autoexit()
        time.sleep(self.__clk<<1)
        self.__kill=True

    def start(self):
        self.__mian=throws(self.__always)

    def join(self):
        self.autoexit()
        self.__mian.join()
