# -*- coding: utf-8 -*-
# favorite_languages = {
# 	'chenkaifan':'python',
# 	'zhangdd':'c',
# 	'chenqiqi':'ruby',
# 	}
# print("chenqiqi's favorite language is "+ favorite_languages['chenqiqi']+"。")

favorite_languages = {
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],
	}

for name,languages in favorite_languages.items():
	# 列表的长度如何确定？
	# if len(languages) == 1:
	# 	print("\n"+ name.title() +"'s favorite language is "+ languages.title() + ".")
	# else:
		print("\n"+ name.title() + "'s favorite languages are:")
		for language in languages:
			print("\t" + language.title())