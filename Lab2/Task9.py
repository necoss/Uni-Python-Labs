# Создайте программу, которая проверяет, является ли множество подмножеством другого.

def isSubsetOfSet(set1, set2):
	return set1.issubset(set2)

setA = {1,2,3}
setB = {1,2,3,4,5,6}

if isSubsetOfSet(setA, setB):
	print('set A is a subset of set B')
else:
		print('set A is NOT a subset of set B')