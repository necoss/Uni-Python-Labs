# Напишите программу, которая выводит числа от N до 1.

def printReversedCountdown(n):
	for i in range(n, 0, -1):
		print(i)

n = 5
printReversedCountdown(n)