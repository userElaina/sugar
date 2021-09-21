from urllib.parse import unquote_to_bytes,quote_from_bytes

def bencode(x:all)->bytes:
	if isinstance(x,(bytes,bytearray,memoryview,)):
		x=bytes(x)
	else:
		x=str(x).encode(encoding='utf8')
	return x

def urlencode(s:all)->str:
	return quote_from_bytes(bencode(s))

def urldecode(s:all)->str:
	return unquote_to_bytes(bencode(s)).decode(errors='backslashreplace')

def uniencode(s:str)->str:
	return s.encode(encoding='unicode_escape').decode()
	
def unidecode(s:str)->str:
	return s.encode().decode(encoding='unicode_escape')
