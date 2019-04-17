# -*- coding: utf-8 -*-
# 练习5-8
users = ['chenkaifan','chenmingci','zhangdd','admin']
for user in users:
	if user == 'admin':
		print("Hello admin,would you like to see a status report?")
	else:
		print("Hello "+ user +", thank you for logging in again.")

# 练习5-9
users = []
# for user in users:
# 	if user == 'admin':
# 		print("Hello admin,would you like to see a status report?")
# 	else:
# 		print("Hello "+ user +", thank you for logging in again.")

if users:
	print("Sorry, now we don't need any users.")
else:
	print("We need to find some users.")

# 练习5—10
current_users = ['chenkaifan','chenmingci','chenqiqi','chenyuanbo','zhangdd','zhangtai']
new_users = ['cuijingmiao','zhaochen','chenkaifan','chenqiqi','cat']

for new_user in new_users:
	if new_user in current_users:
		print(new_user+"已被使用，对不起，请使用其他的用户名")
	else:
		print(new_user+" 未被使用，您可以使用")

# 练习5-11
nums = list(range(1,10))# 如何利用range 与list 做出一个数字列表的方法。
for num in nums:
	if num == 1:
		print(str(num)+'st')
	elif num == 2:
		print(str(num)+'nd')
	elif num == 3:
		print(str(num)+'rd')
	else:
		print(str(num)+'th')
# 注意数字不是字符串，不要给数字加上单引号‘’，这会导致数字被认为是字符串的。