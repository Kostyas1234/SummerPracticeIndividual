import random
import sys
n = sys.argv[1]
sum=0
n=int(n)
for number in range(n):
    r=random.uniform(-1,1)
    print("%.4f " % r)
    sum+=r
sum/=n
print("\n%.4f" % sum)
