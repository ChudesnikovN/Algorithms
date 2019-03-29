__author__ = 'Чудесников Никита'

num = input ('Введите натуральное число: ')
chet = 0
nechet = 0
for ch in num:
	if int(ch) % 2 == 0:
		chet +=1
	else:
		nechet += 1
		
print('Четных: {}, нечетных: {}'.format(chet,nechet))
