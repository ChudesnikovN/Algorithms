__author__ = 'Чудесников Никита'


a = ord(input('Введите первую букву'))
b = ord(input('Введите вторую букву'))
print(a)
print(b)
if (a >= 65) and (a <= 90):
    print(abs(a-b), a - 64, b - 64)
if (a >= 97) and (a <= 122):
    print(abs(a - b), a - 96, b - 96)

