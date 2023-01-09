#!/usr/bin/python

import thulac
import errno
import fileinput


seg = thulac.thulac(seg_only=True)
try:
	for line in fileinput.input():
		print(seg.cut(line, text=True))
except IOError as e: 
	if e.errno != errno.EPIPE:
		raise		
		
		
		
#thul.cut_f("input.txt","output.txt") #input.txt=dumps
