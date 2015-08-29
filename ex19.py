def power(x, n = 2):
	sum = 1
	while n > 0:
		sum = sum * x
		n = n - 1
	return sum

print(power(2))
print(power(2, 5))

