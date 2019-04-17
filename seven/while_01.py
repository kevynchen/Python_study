# -*- coding: utf-8 -*-
prompt = "\nTell me something,and I will repeat it to you:"
prompt += "\nEnter 'quit' to end the program."
# message = ""
active = True
while active:
 	message = raw_input(prompt)
 	if message == 'quit':
 		active = False
 	else:
 	 	print(message)