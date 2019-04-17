# -*- coding: utf-8 -*-
class User(object):
	"""dfirst_name,last_nametr
	ing for User"""
	def __init__(self, first_name,last_name,address,telephone_number,login_attempts):
		self.first = first_name
		self.last = last_name
		self.add = address
		self.tel = telephone_number
		self.login_attempts = login_attempts

	def descripe_user(self):
		print("The first name is "+ self.first + ",the last name is "+ self.last + ",and the address is " +
			 self.add + ",finally the telephone number is "+
			 str(self.tel) +".") 

	def greet_user(self):
		print("Hi "+ self.last+ ",welcome to assign our website.")

	def increment_login_attempts(self):
		self.login_attempts = self.login_attempts + 1
		print("The login attempts is " +str(self.login_attempts)+ ".")

	def reset_login_attempts(self):
		self.login_attempts = 0
		print("Your login attempts is "+ str(self.login_attempts)+".")

user_01 = User('chen','kaifan','beijing',13121088895,5)
# user_02 = User('chen','qiqi','xiaxi',18811597866)
# user_03 = User('gu','shangzhi','yunnan',18811177899)

# user_01.descripe_user()
# user_01.greet_user()

# user_02.descripe_user()
# user_02.greet_user()

# user_03.descripe_user()
# user_03.greet_user()
user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.reset_login_attempts()
