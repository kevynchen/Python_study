# -*- coding: utf-8 -*-
banned_users = ['chen','zhang','taige']
user = 'chenkaifan'
if user not in banned_users:
	print(user.title() +", you can write down what you want.")
# 看了一会儿原来运行出错是因为少了一个“+”的字符。