# Дан список чисел. Найдите среднее арифметическое всех элементов.

numbersList = [1,2,3,4,5,6,7]
result = 0
numbersQty = len(numbersList)

for number in numbersList:
	result += number


print(result / numbersQty)