#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math

primes = []
primeSet = set(primes)

def lpf(x):
	result = x
	limit = math.sqrt(x)
	curNumber = 2
	#check for x prime
	while(curNumber < limit):
		if(isPrime(curNumber)):
			if(not curNumber in primeSet):
				primeSet.add(curNumber)
				primes.append(curNumber)
			if(x % curNumber == 0):
				result = curNumber
		curNumber += 1
	return result


def isPrime(curNumber):
		for prime in primes:
			if(curNumber % prime == 0):
				return False
		return True


print lpf(600851475143)