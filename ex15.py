def my_abs(a):
	if not isinstance(a, (int, float)):
		raise TypeError('bad operand type')
	if a >= 0:
		return a
	else:
		return -a
print(my_abs(10))
print(my_abs(-10))
