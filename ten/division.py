# -*- coding: utf-8 -*-
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

print("Give me two numbers,and I will divide them.")
print("Enter 'q' to quit")

while True:
	first_number = raw_input("\nFirst number: ")
	if first_number == 'q':
		break
	else:
		second_number = raw_input("Second_number: ")
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(answer)