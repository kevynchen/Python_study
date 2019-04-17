# -*- coding: utf-8 -*-
languages = ['Python','Java','c++','C','Ruby','javascript']
print(languages)

print("The first three items in the list are:")
print(languages[:3])

print("Three items from the middle of the list are:")
print(languages[1:4])

print("The last three items in the list are:")
print(languages[-3:])

# 这是第二节
pizzas = ['chenkaifan','chenmq','zhantai','zdd']
for pizza in pizzas:
	print("I like " + pizza +" pizza.")

print("I really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append('chen')
friend_pizzas.append('zhang')

print("My favourite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friends's favourite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)

