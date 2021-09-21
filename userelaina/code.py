'''
`bencode` `urlencode` `urldecode` `uniencode` `unidecode`

`Hash` `hashencode` `hashdecode`

`ahash` `dhash` `phash` `hm`

	>>> bencode(s:all)->bytes
	>>> urlencode(s:all)->str
	>>> urldecode(s:all)->str
	>>> uniencode(s:str)->str
	>>> unidecode(s:str)->str

	>>> Hash(api:str,mem=1<<25)
	>>> hashencode(s:all,api:str,isfile=False,size:int=None,types=bytes)->Union[bytes,str,int]
	>>> hashdecode(s:all,api:str,isfile=False,size:int=None,types=bytes)->Union[bytes,str]

	>>> ahash(pth:str)->int
	>>> dhash(pth:str)->int
	>>> phash(pth:str)->int
	>>> hm(h1:int,h2:int)->int
'''

from userelaina._other import bencode,urlencode,urldecode,uniencode,unidecode
from userelaina._hash import Hash,hashencode,hashdecode
from userelaina._pic import ahash,dhash,phash,hm