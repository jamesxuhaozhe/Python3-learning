def calc(numbers):
	sum = 0
	for x in numbers:
		sum = sum + x * x
	return sum

def calc1(*numbers):
	sum = 0
	for x in numbers:
		sum = sum + x * x
	return sum

numbers = [1, 2, 3, 4, 5]
print(calc(numbers))
print(calc1(*numbers)) 
