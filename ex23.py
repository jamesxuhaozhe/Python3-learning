def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n - 1)

print(fact(1))
print(fact(2))
print(fact(10))
print(fact(11))
