# Дан кортеж чисел. Удалите все элементы, которые делятся на 3 без остатка.

def deleteTupleElements(elem):
	result = tuple(x for x in elem if x % 3 != 0)
	return result

numbers = (1,3,4,6,7,9,12,14)

print(f'Result: {deleteTupleElements(numbers)}')					