import math

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) :
        l=[]
        if x==1:
            max_i=1
        else:
            max_i = int(math.log(bound, x))
        if y==1:
            max_j=1
        else:
            max_j = int(math.log(bound, y))
        for i in range(0,max_i+1):
            for j in range(0,max_j+1):
                if int(x**i+y**j)<=bound:
                    l.append(int(x**i+y**j))
        l=list(set(l))
        return l

A=Solution()
print(A.powerfulIntegers(2,1,10))