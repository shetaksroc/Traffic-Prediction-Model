from numpy import genfromtxt
my_data = genfromtxt('d1_0.csv', delimiter=',')
for i in my_data:
	print i