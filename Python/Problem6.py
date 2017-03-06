n = 100

sumOfSquares = 0
curSum = 0
for i in range(1,n + 1):
	sumOfSquares += i ** 2
	curSum += i

squareOfSums = curSum ** 2
print("Sum of Squares = " + str(sumOfSquares))
print("Square of Sums = " + str(squareOfSums))

print (curSum ** 2) - sumOfSquares
