n = 20

def isPrime(curNumber, primes):
	for prime in primes:
		if(prime * prime > curNumber):
			return True
		elif(curNumber % prime == 0):
			return False
	return True

def primesUnder(x):
	curNum = 2
	primes = []
	while(curNum < x):
		if(isPrime(curNum, primes)):
			primes.append(curNum)
		curNum = curNum + 1
	return primes

def expForPrime(x, prime):
	exp = 0
	while(x % (prime ** (exp + 1)) == 0):
		exp = exp + 1
	return exp

primesList = primesUnder(n)

primesCovered = {x: 0 for x in primesList}

for x in range(1, n+1):
	for p in primesList:
		requiredExp = expForPrime(x, p)
		if(primesCovered[p] < requiredExp):
			primesCovered[p] = requiredExp

result = 1
for p in primesCovered:
	result = result * (p ** primesCovered[p])

print(str(result))
