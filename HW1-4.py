__author__ = 'Чудесников Никита'


#случайное целое число;
#случайное вещественное число;
#случайный символ.
import random

answer = ''
print ('Если хотите целое число - нажмите 1, если хотите вещественное - 2, если символ - 3')
answer = input ()
if answer == '1':
    a = int(input('Введите начало диапазона'))
    b = int(input('Введите конец диапазона'))
    print (random.randint(a,b))
elif answer == '2':
    a = int(input('Введите начало диапазона'))
    b = int(input('Введите конец диапазона'))
    print(random.uniform(a,b))
elif answer == '3':
    a = ord(input('Введите начало диапазона'))
    b = ord(input('Введите конец диапазона'))
    print (chr(random.randint(a,b)))