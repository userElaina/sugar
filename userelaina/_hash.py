import os
import zlib
import hashlib
from typing import Union

from userelaina._other import bencode

hash_len={
	'adler32':4,
	'crc32':4,
	'md5':16,
	'sha1':20,
	'blake2s':32,
	'blake2b':64,
	'sha224':28,
	'sha256':32,
	'sha384':48,
	'sha512':64,
	'sha3_224':28,
	'sha3_256':32,
	'sha3_384':48,
	'sha3_512':64,
	'shake_128':0,
	'shake_256':0,
}

hash_block={
	'adler32':16384,
	'crc32':16384,
	'md5':64,
	'sha1':64,
	'blake2s':64,
	'blake2b':128,
	'sha224':64,
	'sha256':64,
	'sha384':128,
	'sha512':128,
	'sha3_224':144,
	'sha3_256':136,
	'sha3_384':104,
	'sha3_512':72,
	'shake_128':168,
	'shake_256':136
}

class Hash:
	def __init__(self,api:str,mem:int=1<<25):
		self.clear(api,mem)
		self.d=self.digest
		self.b=self.digest
		self.h=self.hexdigest
		self.i=self.intdigest
		self.u=self.update
		self.uf=self.updatefile

	def clear(self,api:str=None,mem:int=None):
		if not api:
			api=self.api
		if api not in hash_block:
			raise TypeError(api+' not in this module')

		if mem is not None:
			self.mem1=mem>>1

		if api=='adler32':
			self._prev=1
			self._f=zlib.adler32
		elif api=='crc32':
			self._prev=0
			self._f=zlib.crc32
		else:
			self._prev=hashlib.new(api,b'')

		self.mem1=mem>>1
		self.block_size=hash_block[api]
		while self.block_size<self.mem1:
			self.block_size=self.block_size<<1
		self.api=api

	def digest(self,size:int=None)->bytes:
		if self.api in ('shake_128','shake_256'):
			return self._prev.digest(size if isinstance(size,int) else 128)
		
		if self.api in ('adler32','crc32'):
			ans=(self._prev&0xffffffff).to_bytes(4,'little')
		else:
			ans=self._prev.digest()

		if not isinstance(size,int):
			return ans
		return (ans+b''*(size-len(ans))) if size>len(ans) else ans[:size]
	
	def hexdigest(self,size:int=None)->str:
		return self.digest(size).hex()
	
	def intdigest(self,size:int=None)->int:
		return int.from_bytes(bytes=self.digest(size),byteorder='little',)

	def update(self,b:bytes):
		if self.api in ('adler32','crc32'):
			self._prev=self._f(b,self._prev)
		else:
			self._prev.update(b)

	def updatefile(self,pth:str)->bytes:
		with open(pth,'rb') as f:
			data=f.read(self.block_size)
			while data:
				self.update(data)
				data=f.read(self.block_size)

def hashencode(
	s:all,
	api:str,
	isfile:bool=False,
	size:int=None,
	types:type=bytes,
)->Union[bytes,str,int]:
	if api not in hash_block:
		raise TypeError(api+' not in this module')
	_a=Hash(api)
	if isfile:
		_a.uf(s)
	else:
		_a.u(bencode(s))

	types=str(types).lower()
	if 'bytes' in types:
		return _a.d(size)
	if 'str' in types:
		return _a.h(size)
	if 'hex' in types:
		return _a.h(size)
	if 'int' in types:
		return _a.i(size)
	return _a.d(size)

def hashdecode(
	s:all,
	api:str,
	isfile:bool=False,
	size:int=None,
	types:type=bytes,
)->Union[bytes,str]:
	if api not in hash_block:
		raise TypeError(api+' not in this module')
	h=b'np==np iff p==0 or n==1'
	types=str(types).lower()
	if 'bytes' in types:
		return h
	if 'str' in types:
		return h.decode('utf8')
	if 'hex' in types:
		return h.hex()
	return h