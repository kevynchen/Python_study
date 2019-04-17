visitors = ['chenqiqi','chenyuanbo','zhangdd','zhangtai','chenmingci']
print(visitors)
# print("I want to invite "+ visitors + " to my party!")


print(visitors[1] + "can not go to my party!")
visitors[1] = 'cuijingmiao'
print(visitors)

print("\nI hava find out a bigger table for us to have dinner!")
visitors.insert(0,'donggg')
visitors.insert(3,'zhaochen')
visitors.append('chenjinchao')
print(visitors)

print("Sorry,because of some trouble,I just can invite for two people to have dinner with me.")
f01_poped = visitors.pop()
print(f01_poped + ", I am so sorry,I really want to invite you to my dinner,however,because of some trouble,I can invite you.")

s02_poped = visitors.pop()
print(s02_poped + ", I am so sorry,I really want to invite you to my dinner,however,because of some trouble,I can invite you.")

t03_poped = visitors.pop()
print(t03_poped + ", I am so sorry,I really want to invite you to my dinner,however,because of some trouble,I can invite you.")

f04_poped = visitors.pop()
print(f04_poped + ", I am so sorry,I really want to invite you to my dinner,however,because of some trouble,I can invite you.")

f05_poped = visitors.pop()
print(f05_poped + ", I am so sorry,I really want to invite you to my dinner,however,because of some trouble,I can invite you.")

s06_poped = visitors.pop()
print(s06_poped + ", I am so sorry,I really want to invite you to my dinner,however,because of some trouble,I can invite you.")

print(visitors[0],visitors[1] + " You two guys are very lucky,I will also invite you to my paity.")

del visitors[0]
del visitors[0]
print(visitors)
