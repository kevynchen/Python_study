# -*- coding: utf-8 -*-
class Restaurant(object):
	"""docstring for restaurant"""
	def __init__(self, restaurant_name,curisine_type):
		self.name = restaurant_name
		self.type = curisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("The restaurant's name is "+ self.name + ",and its' type is " + self.type +".")

	def open_restaurant(self):
		print(self.name+ "is opening now!")

	def set_number_served(self,number_served_1):
		self.number_served = number_served_1

	def increment_served(self,number_served_2):
		self.number_served += number_served_2

# restaurant = Restaurant('guoqiaomixian','beautiful')
# restaurant.number_served = 12
# print("The restaurant's name is "+ restaurant.name + ",and its' type is " + restaurant.type +".")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant_01 = Restaurant('kengdeji','good')
# restaurant_02 = Restaurant('maidanglao','perfect')
# restaurant_01.describe_restaurant()
# restaurant_02.describe_restaurant()
# print("有 "+str(restaurant.number_served)+" 人在这家餐厅就餐过!")

# restaurant.set_number_served(23)
# print("有 "+str(restaurant.number_served)+" 人在这家餐厅就餐过!")

# restaurant.increment_served(23)
# print("有 "+str(restaurant.number_served)+" 人在这家餐厅就餐过!")

class IceCreamStand(Restaurant):
	"""docstring for IceCreamStand"""
	def __init__(self, restaurant_name,curisine_type):
		super(IceCreamStand, self).__init__(restaurant_name,curisine_type)
		self.flavors = []

	def show_flavors(self):
		print("这家冰激凌店有很多种口味，分别是：")
		for flavor in self.flavors:
			print(flavor)

iceCreamStand = IceCreamStand('xiaomi','excellent')
iceCreamStand.flavors = ['haochide','delicious','good','perfect']
iceCreamStand.show_flavors()


		