__author__ = 'Чудесников Никита'

import random
num = random.randint (0,100)
cnt = 0
print (num)
while cnt < 10:
	user_num = int(input('Введите число '))
	if user_num == num:
		print ('Угадал!')
		break
	elif num > user_num:
		print ('больше')
	else:
		print ('меньше')
	cnt += 1
	if cnt == 10:
		print('число: ',num)