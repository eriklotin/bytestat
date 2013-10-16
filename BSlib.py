# -*- coding: utf-8 -*-
import sys
import struct

def analizeFile(filepath=""):
	try:
		fp = open(filepath, 'rb')
	except:
		return False, u"Error reading file"
		
	statArr = [0 for i in range(256)]
	
	b = fp.read(1)
	while b != '':
		statArr[ord(b)] += 1
		b = fp.read(1)
	
	output = ""
	for i in range(256):
		binstr = bin(i)[2:]
		while len(binstr) < 8:
			binstr = '0'+binstr
		output += "%03d | %8s: %d\n" % (i, binstr, statArr[i])
	fp.close()
	return True, output