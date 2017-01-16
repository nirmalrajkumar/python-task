import sys

def ni():
	fr = file('/home/asm/Documents/nirmal/test12.txt','r')
	a=fr.readlines()
	try:
		for b in a:
			c = b.split(" ")
			print c[1]
	except Exception:
		pass
ni()
	           


