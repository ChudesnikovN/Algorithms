__author__ = 'Чудесников Никита'



year = int(input('Введите год'))

if (year % 100 != 0) and (year % 4 == 0):
    print('вискосный')
elif year % 400 == 0:
    print('високосный')
else:
    print('невискосный')