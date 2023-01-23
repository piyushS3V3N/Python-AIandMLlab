# Implementation of prime number check in python

def prime_check(x):

	flag = True

	for i in range (2,x):
		if(x%i == 0):
			flag = False
			return flag

	return flag


if __name__ == "__main__":
	print("7 is a prime number? : " + str(prime_check(7)))
	print("9 is a prime number? : " + str(prime_check(9)))