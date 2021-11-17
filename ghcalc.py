i = 1

while i == 1:
	print("калькулятор")
	print()
	num1 = float(input("Ведіть перше чисо:  "))
	num2 = float(input("Ведіть друге чисо:  "))
	print("Операції")
	print()
	print("1 - додавання")
	print("2 - віднімання")
	print("3 - множення")
	print("4 - ділення")
	print()
	vybir2 = float(input('Zrobit vybir:  '))
	print()
	if vybir2 == 1:
		rezult = num1 + num2
		print("додавання dvoch:  " + srt(rezult))
	elif vybir2 == 2:
		rezult = num1 - num2
		print ("віднімання:  " + str(rezult))
	elif vybir2 == 3:
		rezult = num1 * num2
		print("додавання:  " + str(rezult))
	elif vybir2 == 4:
		rezult = num1 / num2
		rint("ділення:  " + str(rezult))
		print()
	print("1 - продовжити")
	print("2 - завершити ")
	
	vubir = int(input('Зробіть свій вибір: '))
	print()
	if vubir == 1:
		i = 1 
	elif vubir == 2:
		i = 0				