class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s=reversed(s)
        # l=0
        # space=0
        # for i in s:
        #     if i==" ":
        #         space=1
        #         break
        #     else:
        #         l=l+1
        # if space==0:
        #     return 0
        # else:
        #     return l
        return len(s.split()[-1]) if s.split() else 0




A=Solution()
print(A.lengthOfLastWord("world"))