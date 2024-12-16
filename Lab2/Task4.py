# Напишите программу, которая находит количество делителей числа N.

def countDivisors(n):

	divisorsCount = 0

	if n<=0:
		return 'Print n that will be > 0'

	for i in range(1, n+1):
		if n % i == 0:
			divisorsCount += 1
		
	return divisorsCount

n = 12

print(f'Quantity of Divisors for number {n}: {countDivisors(n)}')