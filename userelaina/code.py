'''
`b` `int` `url` `uni`

`hash` `hash_len`

	>>> bencode(s:str)->bytes
	>>> bdecode(s:str,p=('',False,))->bytes
	>>> intencode(s:all)->int
	>>> intdecode(s:int)->bytes

	>>> hash_len={str:int}
	>>> hashencode(s:all,api:str,need_size=128,block_size=0,types:str)->Union[bytes,str]
	>>> hashdecode(s:all,api:str,block_size:=0,types:str)->Union[bytes,str]
'''

from userelaina._basic import bencode,bdecode,intencode,intdecode
from userelaina._other import urlencode,urldecode,uniencode,unidecode
from userelaina._hash import hashencode,hashdecode,hash_len