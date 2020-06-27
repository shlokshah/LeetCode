class Solution:
    def trailingZeroes(self, n: int) -> int:
        i=1
        temp=0
        while 5**i<=n:
            temp=temp+n//5**i
            i+=1
        return temp

A=Solution()
print(A.trailingZeroes(5))