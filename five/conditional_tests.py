# -*- coding: utf-8 -*-
# 5-1练习
car = 'bmw'
print("Is car == 'bmw',I think it is true.")
print("car == 'bmw'")
print("\nIs car == 'audi',I think it is false.")
print("car == 'audi'")

# 5-2练习
# 关键字是否在列表或者不在列表中
roommates = ['chenkaifan','zhangdd','zhangtai']
roommate = 'chenqiqi'
roommate_01 = 'chenkaifan'
if roommate not in roommates:
	print(roommate.title()+", he went home yesterday.")

if roommate_01 in roommates:
	print(roommate_01.title()+", he is a good guy.")