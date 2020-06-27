class Solution:
    def titleToNumber(self, s: str) -> int:
        s=list(s)
        sum=0
        for i in range(len(s)):
            sum+=(26**(len(s)-1-i))*(ord(s[i])-64)
        return sum

A=Solution()
print(A.titleToNumber("A"))

# ZY= 701
# AB=28