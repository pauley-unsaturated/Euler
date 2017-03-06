def reverse(string):
	if(string == ""):
		return ""
	return reverse(string[1:]) + string[0]


def isPalindrome(x):
	xStr = str(x)
	return xStr == reverse(xStr)

biggest = 0
i = 1000;
while ( i > 100 ):
	j = 1000
	while ( j >= i ):
		if( isPalindrome( i * j ) ):
			if(biggest < i * j):
				biggest = i * j
				print "found " + str(i * j)
		j = j - 1
	i = i - 1
