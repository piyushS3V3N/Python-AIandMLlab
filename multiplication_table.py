# Implementation of multiplication table in python

def multiplication_table(x):
	for i in range(1,11):
		print("\n{:^24s}| {} X {} : {} |\n".format("",x, i , (x*i)))


multiplication_table(5)