# -*- coding: utf-8 -*-
# user_0 = {
# 	'username':'chenkaifan',
# 	'first':'chen',
# 	'last':'kaifan',
# 	}
# for k,v in user_0.items():
# 	print("\nKey: "+k)
# 	print("Value: "+v)



# 遍历字典中的所有键
favorite_languages = {
	'chen':'Ruby',
	'zhang':'c',
	'chenqiqi':'java',
	'zhangdd':'javascript',
	}

friends = ['chen','zhangdd']
not_friends = ['chenqiqi','zhang']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
# 		print("Hello "+ name.title()+ " I see your favorite language is "+ 
# 			favorite_languages[name]+ "!")

# if 'chenyuanbo' not in favorite_languages.keys():
# 	print("chenyuanbo,please take our poll!")

# 练习6-6的部分代码，接上面的。（遍历字典中的所有键）
		print("Thank you for your poll, "+ name)
	else:
		print(name+ ",please take our poll!") 


