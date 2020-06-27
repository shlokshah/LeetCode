class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            a=haystack.index(needle)
            return a
        except:
            return -1


A=Solution()
print(A.strStr("hello","aa"))
