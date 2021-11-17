i = 1

while i == 1:
	print()
	print ("Глибина коду")
	print()

	print('Функції програми:  ')
	print()
	print('1 - Калькулятор')
	print('2 - Конвертер')
	print('3 - градусник')
	print()

	vybir = int(input('Зробіть вибір:  '))
	print(vybir)
	
	#Калькулятор
	if vybir == 1:
		j = 1
		while j == 1:
			print("Ви вибрали калькулятор")
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
			else:
				print("EROR")
			
			print("1 - продовжитив використання калькулятор")
			print("0 - завершити використання калькулятора")
			j = int(input("Зробіть вибір:"))

	#Конвертер
	elif vybir == 2:
		g = 1
		while g == 1:

			print()
			print("Ви вибрали Конвертер")
			print()
			hrn = float(input("Ведіть суму для обміну:  "))
			dol = float(input("Ведіть курс долара:  "))
			evro=float(input("Ведіть курс євро:  "))
			pounts=float(input("Ведіть курс фунтів:  "))

			doll = hrn/dol
			ev = hrn/evro
			pountes = hrn/pounts

			print()
			print("Ви отримаїте: Долар " + str(round(doll, 2)))
			print("Ви отримаїте: Євро " + str(round(ev, 2)))
			print("Ви отримаїте: Фунти " + str(round(pountes, 2)))	
			print()
			
			print("1 - продовжитив використання конвертеру")
			print("0 - завершити використання конвертеру")
			g = int(input("Зробіть вибір:"))

		#Градусник
	elif vybir == 3:
		h = 1
		while h == 1:

			print("Ви вибрали градусник")
			print()
			print("Види градусників:")
			print("1 - простий")
			print("2 - Складний")
			vybir1 = int(input("Оберіть тип термометра:    "))
		#Простий
			if vybir1 == 1:
				print()
				print("Ви вибрали тип: Простий")
				print()
				a = int(input('Ведіть температуру повітря:  ')) 
				if a <= 0:
					print("Сьогодні холодно")
				elif a >= 0:
					print("Сьогодні тепло")
				print("1 - продовжитив використання градусника")
				print("0 - завершити використання гардусника")
				h = int(input("Зробіть вибір:"))


		#Складний
			elif vybir1 == 2:
				h = 1
				while h == 1:

					print()
					print("Ви вибрали тип: Складний")
					print()
					a = int(input('Ведіть температуру повітря:  '))
					if a < 0:
						print("Сьогодні прохолодно,візьми куртку")
					elif a > 0 and a <= 15:
						print("Сьогодні прохолодно,вдягнись тепліше")
					elif a >= 15 and a <= 30:
						print("Сьогодні тепло,можна одягнутись легко")
					elif a > 30:
						print("Сьогодні спекотно")

					else:
						print("Такої функції нема")

					
					print("1 - продовжитив використання градусника")
					print("0 - завершити використання гардусника")
					h = int(input("Зробіть вибір:"))
	
	print()
	print("1 - почати заново")
	print("0 - вийти")
	i = int(input("Зробіть вибір:"))