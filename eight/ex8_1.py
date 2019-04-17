# -*- coding: utf-8 -*-
# 练习8-1
def make_shirt(chima,word):
	print("The T-shirt is "+ chima+" big.And some words like "+ word +"are written on it.")

make_shirt('33','I love you!')

# 练习8-2
def make_shirt(chima,word = 'I love Python'):
	print(word + " are written on the "+chima+" T-shirt.")

make_shirt('big')
make_shirt('medium')
make_shirt('small','I love ruby')


