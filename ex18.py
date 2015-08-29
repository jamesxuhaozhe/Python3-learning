def apd_end(l = None):
	if l is None:
		l = []
	l.append('end')
	return l
print(apd_end())
print(apd_end([1, 2]))
