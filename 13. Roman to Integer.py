class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        dictionary={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,}
        sum=0
        for i in range(n-1):
            if dictionary[s[i+1]]>dictionary[s[i]]:
                sum=sum-dictionary[s[i]]
            else:
                sum=sum+dictionary[s[i]]
        sum += dictionary[s[n - 1]]
        return sum

A=Solution()
print(A.romanToInt("V"))