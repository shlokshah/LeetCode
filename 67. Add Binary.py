class Solution:
    def addBinary(self, a: str, b: str):
        # carry=k=0
        # lena=len(a)
        # lenb=len(b)
        # i=lena-1
        # j=lenb-1
        # ans=""
        # while k<(lena+lenb):
        #     if i>-1 and j>-1:
        #         temp=carry+int(a[i])+int(b[j])
        #         if temp>1:
        #             temp=temp%2
        #             carry=1
        #         ans=str(temp)+ans
        #         i-=1
        #         j-=1
        #         k+=1
        #     elif i>-1 and j<0:
        #         temp = carry + int(a[i])
        #         if temp > 1:
        #             temp = temp % 2
        #             carry = 1
        #         ans=str(temp)+ans
        #         i -= 1
        #         k += 1
        #     elif i<0 and j>-1:
        #         temp = carry + int(b[j])
        #         if temp > 1:
        #             temp = temp % 2
        #             carry = 1
        #         ans=str(temp)+ans
        #         j -= 1
        #         k += 1
        #
        # return str(ans)
        pass


A=Solution()
print(A.addBinary("11", "1"))