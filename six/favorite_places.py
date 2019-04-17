# -*- coding: utf-8 -*-
favorite_places = {
	'chenkaifan':['beijing','tianjin','shanghai'],
	'chenmingci':['beijing','guangxi','jilin'],
	'chenqiqi':['nanning','shanxi','xiamen'],
	}

for name,places in favorite_places.items():
	# print("\n" + name.title() + "'s favorite places are: ")
	# for place in places:
	# 	print("\t"+ place)
	for place in places:
		print("\n" + name.title() + "'s favorite places are: "+ place+ ".")
		
