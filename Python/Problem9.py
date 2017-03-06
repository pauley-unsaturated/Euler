#a ** 2 + b ** 2 = c ** 2
# and a + b + c = 1000
from math import sqrt

for a in range(2,998):
  for b in range(a,997):
    c = sqrt(a ** 2 + b ** 2)
    if(c == int(c)):
      c = int(c)
      if(a + b + c == 1000):
        print "a:" + str(a) + " b:" + str(b) + " c:" + str(c)
        print a * b * c
