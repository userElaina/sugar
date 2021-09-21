import cv2
import numpy as np

def ahash(pth:str)->str:
    try:
        img=cv2.imread(pth,cv2.IMREAD_UNCHANGED)
        img=cv2.resize(img,(8,8),cv2.INTER_AREA)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    except:
        return -1

    avg=np.mean(img)
    ans=0
    for i in img:
        for j in i:
            ans=(ans<<1)|(0 if j<avg else 1)
    return ans

def dhash(pth:str)->str:
    try:
        img=cv2.imread(pth,cv2.IMREAD_UNCHANGED)
        img=cv2.resize(img,(9,8),cv2.INTER_AREA)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    except:
        return -1

    ans=0
    for i in img:
        l=None
        flg=True
        for j in i:
            if flg:
                l=j
                flg=False
                continue
            ans=(ans<<1)|(0 if j<l else 1)
            l=j
    return ans

def phash(pth:str)->str:
    try:
        img=cv2.imread(pth,cv2.IMREAD_UNCHANGED)
        img=cv2.resize(img,(32,32),cv2.INTER_AREA)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    except:
        return -1

    img=cv2.dct(np.float32(img))[0:8,0:8]
    avg=np.mean(img)
    ans=0
    for i in img:
        for j in i:
            ans=(ans<<1)|(0 if j<avg else 1)
    return ans

def hm(h1:int,h2:int)->int:
    h,d=0,h1^h2
    while d:
        h+=1
        d&=d-1
    return h
