i = 1

while i == 1: #працює	

	print ("-_-_-_-ПРОДУКТОВИЙ-_-_-_-")
	print()

	print()
	print("1 - овочі")
	print("2 - фрукти")
	print("3 - все разом")
	print()
	a = int(input('виберіть що ви взяли:  '))
	print()
	if a == 1:
		h = 1
		while h == 1:
			print("1кг = 30 грн")
			print("більше 100кг знишка 0.05%")
			print()
			b = int(input("Ведіть скільки ви взяли в кг:"))
			print()
			if b <= 100:
				print(b)
				print("знишки нема")
				print()
				znushka = b * 30 
				print("чек: грн " + str(round(znushka,2)))
				print("без знишки")
			elif b > 100:
				print(b)
				print("ви взяли")
				print()
				print("разом зi знишко виходить")
				c = b * 100
				znushka = b * 30 * 0.05
				suma = c - znushka
				print ("чек: грн " + str(round(suma,2)))
				print("разом зi знишко")
			print()
			print("1 - продовжитив використання")
			print("0 - завершити використання")
			h = int(input("Зробіть вибір:"))

	if a == 2:
		h = 1
		while h == 1:	
			print("1кг = 150 грн")
			print("більше 100кг знишка 0.07%")
			print()

			b = int(input("Ведіть скільки ви взяли в кг:"))
			print()
			if b < 150:
				print(b)
				print("знишки нема")
				print()
				znushka = b * 150 
				print("чек: грн " + str(round(znushka,2)))
				print("без знишки")
			elif b >= 150:
				print(b) 
				print("ви взяли")
				print()
				print("разом зi знишко виходить")
				c = b * 150 
				znushka = b * 150 * 0.07
				suma = c - znushka	
				print ("чек: грн " + str(round(suma,2)))
				print("разом зi знишко")
			print()
			print("1 - продовжитив використання")
			print("0 - завершити використання")
			h = int(input("Зробіть вибір:"))
	if a == 3:
		h = 1
		while h == 1:
			print("1кг = 180 грн")
			print("більше 200кг знишка 0.12%")
			print()


			b = int(input("Ведіть скільки ви взяли в кг:"))
			print()
			if b <= 200:
				print(b)
				print("знишки нема")
				print()
				znushka = b * 180 
				print("чек: грн " + str(round(znushka,2)))
			elif b >= 200:
				print(b)
				print("ви взяли")
				print()
				print("разом зi знишко виходить")
				print()
				c = b * 180
				znushka = b * 180 * 0.12
				suma = c - znushka

				
				print ("чек: грн " + str(round(suma,2)))


			print("1 - продовжитив використання")
			print("0 - завершити використання")
			h = int(input("Зробіть вибір:"))
	print()
	print("1 - почати заново")
	print("0 - вийти")
	i = int(input("Зробіть вибір:"))