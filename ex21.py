def func(name, age, **kw):
	print('name', name, 'age', age, 'others:', kw)
func('James', 6)
func('JamesXu', 21, city = 'Changzhou')

def address(number, street, **other):
	print('number', number, 'street', street, 'other', other)

address('704', 'Sierra Vista Ave', zipcode = 91801, city = 'Alhambra')

