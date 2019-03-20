__author__ = 'Чудесников Никита'

#3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

x1 = int(input("Input x1"))
y1 = int(input("Input y1"))
x2 = int(input("Input x2"))
y2 = int(input("Input y2"))

if x1 == x2:
    print ('x = ',x1)
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print('y = {}x + {}'.format(k,b))