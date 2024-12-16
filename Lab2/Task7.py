# Создайте программу, которая генерирует словарь с ключами от 1 до N, а значениями — квадраты чисел.

def generateSquareDict(n):
	if n<=0:
		return 'Enter n > 0'
	
	squareDict = {i: i**2 for i in range(1, n+1)}
	return squareDict

n = 5
print(f'Result Dict: {generateSquareDict(n)}')