'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs) :
        if len(strs)==0:
            return ""

        s=""
        min_length=10000

        for i in strs:
            if len(i)<min_length:
                min_length=len(i)

        for i in range(min_length):
            temp=strs[0][i]
            flag=0
            for j in strs[1:]:
                if j[i]!=temp:
                    flag=1
                    break
            if flag==0:
                s=s+temp
            else:
                break
        return s

A=Solution()
print(A.longestCommonPrefix(["aca", "cba"]))