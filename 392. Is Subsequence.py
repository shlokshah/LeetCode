class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start=-1
        for i in s:
            start=t.find(i, start+1)
            if start==-1: return False
        return True


A=Solution()
print(A.isSubsequence('aaaaaa',"bbaaaa"))