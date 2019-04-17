# -*- coding: utf-8 -*-
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

# 添加键-值对
alien_0 = {'color':'blue','points':5}

alien_0['x position'] = 0
alien_0['y position'] = 25
print(alien_0)

# 修改字典中的值
alien_0 = {'x_position':0,'y_position':25,'speed':'meduim'}
print("初始位置是"+ str(alien_0['x_position'])+".")
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
 	x_increment = 1
elif alien_0['speed'] == 'meduim': # 不要老是搞错全等于号== 与赋值=的区别，这里是全等于的意思。
 	x_increment = 2
else:
 	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("外星人新的位置是"+ str(alien_0['x_position']))

