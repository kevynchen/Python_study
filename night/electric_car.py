# -*- coding: utf-8 -*-
class Car(object):
	"""一次模拟汽车的属性"""

	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year)+ ' '+self.make +' '+self.model
		return long_name.title()

	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has "+ str(self.odometer_reading)+" miles on it.")

	def update_odometer(self,mileage):
		"""将里程表读数设置为指定的值"""
		self.odometer_reading = mileage

	def increment_odometer(self,miles):
		"""将里程增加为指定的量"""
		self.odometer_reading += miles 

	def fill_gas_tank(self):
		print("This car has a gas tank.")

# my_new_car = Car('audi','a4',2016)
# print(my_new_car.get_descriptive_name())
# # my_new_car.odometer_reading = 23 # 直接修改属性的值
# my_new_car.update_odometer(23500)
# my_new_car.read_odometer() 

# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()

# 将实例用作属性
class Battery(object):
	"""一次模拟电动汽车的尝试"""

	def __init__(self, battery_size=70):
		"""初始化电瓶的属性"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print("This car has a "+ str(self.battery_size)+"-kwh battery.")

class ElectricCar(Car):
	"""电动汽车的特殊之处"""
	def __init__(self, make,model,year):
		super(ElectricCar, self).__init__(make,model,year)
		self.battery = Battery()
		#self.battery_size = 70

	# def describe_battery(self):
	# 	"""打印一条描述电瓶容量的消息"""
	# 	print("This car has a "+ str(self.battery_size)+"-kwh battery.")

	def fill_gas_tank(self):
		print("This car doesn't need a gas tank!")
	
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() # 特殊的属性
my_tesla.fill_gas_tank() # 重写父类的方法


		
