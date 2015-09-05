import sys

def open_file():
	return open(sys.argv[1], 'r')

file = open_file()

for line in file:
	print(len(line.strip().split(' ')))

file.close()
	
