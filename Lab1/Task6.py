# Напишите программу, которая удаляет все элементы списка, встречающиеся более одного раза

from collections import Counter

def removeDuplicates(list):
	duplicatesQty = Counter(list)

	result = [item for item in list if duplicatesQty[item] == 1]
	return result

list = [1, 2, 2, 3, 4, 4, 5]

print(f'Edited list: {removeDuplicates(list)}')