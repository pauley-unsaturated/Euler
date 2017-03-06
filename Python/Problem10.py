n = 2000000

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


print reduce(lambda x, y: x + y, primesUnder(n))
