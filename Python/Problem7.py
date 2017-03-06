n = 10001
primes = []

def isPrime(curNumber, primes):
	for prime in primes:
		if(curNumber % prime == 0):
			return False
	return True

x = 2
while(len(primes) < n):
	if(isPrime(x, primes)):
		primes.append(x)
	x = x + 1

print(primes[n - 1])