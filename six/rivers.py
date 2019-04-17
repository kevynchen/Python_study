# -*- coding: utf-8 -*-
# 6-5 河流
rivers = {
	'nile':'egypt',
	'changjiang':'china',
	'huanghe':'china',
	}
for r, c in rivers.items():
 	print("The "+r+" runs through "+ c + ".")

for river in rivers.keys():
 	print(river)
print('\n')
for country in rivers.values():
 	print(country)