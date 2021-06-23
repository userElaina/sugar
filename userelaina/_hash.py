import hashlib
from userelaina._small import *
from userelaina._basic import *

hash_len={
	"md5": 16,
	"sha1": 20,
	"blake2s": 32,
	"blake2b": 64,
	"sha224": 28,
	"sha256": 32,
	"sha384": 48,
	"sha512": 64,
	"sha3_224": 28,
	"sha3_256": 32,
	"sha3_384": 48,
	"sha3_512": 64,
	"shake_128": 0,
	"shake_256": 0,
}

def hash_f(pth:str,api:str,block_size:int)->bytes:
	block_size=trys(block_size,int,1048576)
	with open(pth,'rb') as f:
		hash_b=hashlib.new(api,b'')
		while True:
			data=f.read(block_size)
			if not data:
				break
			hash_b.update(data)
		return hash_b


def hashencode(s:all,api:str,need_size:int=128,block_size:int=0,types:str=None)->Union[bytes,str]:
	if api not in hash_len:
		raise TypeError(api+'not in this module')
	if block_size:
		h=hash_f(s,api,block_size)
	else:
		h=hashlib.new(api,bencode(s))

	if hash_len[api]:
		h=h.digest()
	else:
		h=h.digest(need_size)

	types=str(types).lower()
	if types in {'str','hex','string'}:
		return h.hex()
	if types in {'decode'}:
		return h.decode()
	return h


	return h if types==bytes else h.hex()

def hashdecode(s:all,api:str,block_size:int=0,types:str=None)->Union[bytes,str]:
	h='Are you kidding me?\np==np iff p==0 or n==1!'
	types=str(types).lower()
	if types in {'str','string','decode'}:
		return h
	return h.encode()

