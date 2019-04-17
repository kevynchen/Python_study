# -*- coding: utf-8 -*-
filename = 'programming.txt'
with open(filename,'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love riding.\n")

with open(filename,'a') as file_object:
	file_object.write("I love singing.\n")
	file_object.write("I love my father.\n")