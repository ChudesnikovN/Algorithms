__author__ = 'Чудесников Никита'

ZNAKI = ['+','-','*','/','0']
while True:
	answer = input('Введите выражение: ')
	st = answer.split()
	a = st[0]
	zn = st[1]
	b = st[2]
	
	if zn == '0':
		print ('Завершено')
		break
	if zn not in ZNAKI:
		print ('Вы ввели неправильный знак, повторите ввод')
	if zn == '+':
		print ('Ответ: ', float(a) + float(b))
	if zn == '-':
		print ('Ответ: ', float(a) - float(b))
	if zn == '*':
		print ('Ответ: ', float(a) * float(b))
	if (zn == '/') and (b != '0') :
		print ('Ответ: ', float(a) / float(b))
	elif b == '0':
		print ('На ноль делить нельзя')

		
	