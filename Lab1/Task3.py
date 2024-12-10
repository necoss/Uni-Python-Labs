# Создайте программу, которая находит общие ключи в двух словарях и выводит их значения.

dict1 = {
	'car': 'Porsche',
	'name': 'Alex',
	'age': 19,
	'isStudying': True,
}

dict2 = {
	'isBackendDev': False,
	'name': 'necoss',
	'isStudying': False,
	'car': 'Koeniggsegg',
}

findSameKeys = dict1.keys() & dict2.keys()

for key in findSameKeys:
	print(f"Key: {key}, Items: {dict1[key]} and {dict2[key]}")


# print(findSameKeys)