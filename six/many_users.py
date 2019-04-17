# -*- coding: utf-8 -*-
users = {
	'aeinstein':{
	'first':'albert',
	'last':'einstein',
	'location':'princeton',
	},
	'mcurie':{
	'first':'marie',
	'last':'curie',
	'location':'paris',
	},
}

for username,user_info in users.items():
	print("\nUsename: "+ username)
	full_name = user_info['first'] + ' ' + user_info['last']
	Location = user_info['location']

	print("\t" + full_name)
	print("\t" + Location)

