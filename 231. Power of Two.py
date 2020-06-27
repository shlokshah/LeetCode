import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        try:
            b=math.log(n, 2)
            temp=2**int(b)
            if n==temp:
                return True
            else:
                return False
        except:
            return False

A=Solution()
print(A.isPowerOfTwo(0))