# -*- coding: utf-8 -*-

while True:
	reason_programming = raw_input("Why are you like programming? ")
	filename = 'reason_programming.txt'
	with open(filename,'a') as f_obj:
		f_obj.write(reason_programming) 