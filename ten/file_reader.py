# -*- coding: utf-8 -*-
# with open('pi_digits.txt') as file_object:
# 	contents = file_object.read()
# 	print(contents.rstrip())

# file_path = 'C:\Users\Kaifan\python\pi_digits.txt'
# with open(file_path) as file_object:
# 	contents = file_object.read()
# 	print(contents.rstrip())

filename = 'pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())