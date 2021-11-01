import os
import time
import threading

def getlock():
    return threading.Lock()

lk=getlock()

def lock(x=None,un:bool=False):
    if x is None:
        x=lk
    return x.release() if un else x.acquire()

def unlock(x=None):
    if x is None:
        x=lk
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
        n:int=None,
        clk:float=0,
        f=None,
    ):
        self.__ed=False
        self.__pause=False
        self.__q=list()

        self.__n=n if isinstance(n,int) else os.cpu_count()
        self.__total=0
        self.__finish=0

        self.__f=f
        self.__clk=clk 


    def __iter__(self):
        for i in self.__q.copy():
            yield i

    def __str__(self):
        return '<class nThread with '+str(self.__n)+' threads>'
    def __repr__(self):
        return '<class nThread with '+str(self.__n)+' threads>'

    def __del__(self):
        print('del this nThread; '+str(self.__finish)+'/'+str(self.__total)+' threads are finished')

    def __always(self):
        _l=list()
        while True:
            time.sleep(self.__clk)

            if self.__pause:
                continue

            if self.__ed and not len(_l):
                return
            for i in _l.copy():
                if not i.is_alive():
                    _l.remove(i)
                    self.__finish+=1
            while len(self.__q) and len(_l)<self.__n:
                _l.append(throws(self.__f,self.__q.pop(0)))

    def get_queue(self)->list:
        return self.__q.copy()

    def get_info(self)->dict:
        _d={
            'classname':'nThread',
            'clock':self.__clk,
            'total':self.__total,
            'finished':self.__finish,
            'limited':self.__n,
            'waiting':len(self.__q),
        }
        return _d

    def append(self,args:tuple=tuple()):
        self.__total+=1
        self.__q.append(args)

    def extend(self,l:list):
        if isinstance(l,int):
            l=list(range(l))
        self.__total+=len(l)
        self.__q+=l

    def pause(self):
        self.__pause=~self.__pause

    def start(self):
        self.__mian=throws(self.__always)

    def join(self):
        while len(self.__q):
            time.sleep(self.__clk*2)
        self.__ed=True
        self.__mian.join()
        self.__ed=False

