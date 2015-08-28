def bmi(weight):
	if weight < 18.5:
		print('too thin')
	elif weight <= 25:
		print('normal')
	elif weight <= 28:
		print('overweight')
	elif weight <= 32:
		print('fat')
	else:
		print('too fat')
bmi(19)
