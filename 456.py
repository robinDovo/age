

while True:
	age = input('請輸入年齡：')
	age = int(age)
	if age == -1:
		print('感謝使用本程式,結束')
		break
	if age < 13:
		print('屁孩')
	elif age >= 13 and age < 18:
		print('國中生')
	elif age >= 18 and age < 22:
		print('大學生')
	else:
		print('社會人士')

