__author__ = 'Чудесников Никита'


def howmuch(x,num):
	cnt = 0
	for ch in x:
		if ch == num:
			cnt += 1
	return cnt
	
num = input ('Введите цифру ')
q = int(input ('Введите количество чисел '))
sum = 0

for i in range(0,q):
	x = input ('Введите число ')
	sum += howmuch(x, num)
print ('Итого цифр: ',sum)	