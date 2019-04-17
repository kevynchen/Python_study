# -*- coding: utf-8 -*-
aliens = []

for alien_number in range(0,30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

# for alien in aliens[:5]:
# 	print(alien)
# print("...")

# print("The total number of aliens: "+ str(len(aliens)))
# 在列表里嵌套着字典
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
for alien in aliens[:5]:
	print(alien)
print("...")



