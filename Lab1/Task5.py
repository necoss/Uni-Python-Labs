# Дан список строк. Выведите длину самой короткой строки.

def findShortestString(string):
	if not string:
		return "Empty string"
	
	return min(len(s) for s in string)

string = ['water', 'car', 'number', 'BonAqua', 'GT3RS']

print(f'Length of the Shortest String: {findShortestString(string)}')