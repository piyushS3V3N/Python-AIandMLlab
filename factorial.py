# Implementation of Factorial in python

def factorial(x):
	if(x==1):
		return x

	return factorial(x-1)*x



print(factorial(4))