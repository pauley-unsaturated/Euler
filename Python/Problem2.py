curSum = 2
curFibs = [1, 2]
curIdx = 0

upperLimit = 4000000

while(curFibs[(curIdx + 1) % 2] < upperLimit):
	curFibs[curIdx] = sum(curFibs)
	if(curFibs[curIdx] % 2 == 0):
		curSum += curFibs[curIdx]
	curIdx = (curIdx + 1) % 2
	print curFibs

print curSum