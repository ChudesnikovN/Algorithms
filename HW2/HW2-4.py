__author__ = 'Чудесников Никита'

# 1,-0.5,0.25,-0.125.....

n = int(input ('Введите n '))
summ = 0
for i in range(0,n):
	summ += (0.5 ** i) * (-1)**i 
print (summ)