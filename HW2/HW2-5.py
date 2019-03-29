__author__ = 'Чудесников Никита'

START = 32
END = 127

rows = ((END - START + 1) // 10) + 1
print(rows)
for i in range (0, rows):
	stroka =''
	for j in range (0,10):
		index = START + i + j * rows 
		if index <= END:
			if index < 100:
				str_index = str(index)+ ' '
			else:
				str_index = str(index)
			stroka += str_index + ' '+ chr(index) + ' |'
	print(stroka)	
