from urllib.parse import unquote_to_bytes,quote_from_bytes

from userelaina._small import *
from userelaina._basic import *

def urlencode(s:str)->str:
	return quote_from_bytes(bencode(s))

def urldecode(s:str)->str:
	return unquote_to_bytes(bencode(s)).decode(errors='backslashreplace')

def uniencode(s:str)->str:
	return s.encode(encoding='unicode_escape').decode()
	
def unidecode(s:str)->str:
	return s.encode().decode(encoding='unicode_escape')
