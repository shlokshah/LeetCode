class Solution:
    def plusOne(self, digits):
        i=-1
        n=len(digits)
        while n!=0:
            if digits[i]==9:
                if i+n!=0:
                    digits[i]=0
                    i-=1
                else:
                    digits[i] = 0
                    digits.insert(0, 1)
                    n = 0
            else:
                digits[i]+=1
                n=0
        return digits


A=Solution()
print(A.plusOne([4,2,7,3,8,9]))


