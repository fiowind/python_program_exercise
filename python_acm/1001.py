import math,sys

nums=[]
for line in sys.stdin:
    for word in line.split():
        nums.append(float(word))
    if(int(word)==0):
        break

nums.reverse()
for num in nums:
    print("%.4f"%math.sqrt(num))
