# -*- coding: utf-8 -*-
# def describe_pet(animal_type,pet_name):
def describe_pet(pet_name,animal_type = 'dog'):
	"""显示宠物的信息"""
	print("\nI have a "+animal_type+".")
	print("My "+animal_type+ "'s name is "+ pet_name+".")

describe_pet('david')
describe_pet('chenqiqi','cat')
describe_pet(pet_name = 'chenmingci',animal_type = 'pig')
