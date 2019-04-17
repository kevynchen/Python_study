# -*- coding: utf-8 -*-

while True:
	guest = raw_input("Please enter your name here: ")
	print("Hello,"+guest+".")
	filename = 'guest_book.txt'
	with open(filename,'a') as f_obj:
		f_obj.write(guest+"曾经来过这里！\n")

