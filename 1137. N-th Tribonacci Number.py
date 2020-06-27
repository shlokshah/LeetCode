class Solution:
    def tribonacci(self, n: int) -> int:
        a=0
        b=1
        c=1
        sum=0
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            for _ in range(n-2):
                sum=a+b+c
                a = b
                b=c
                c=sum
            return sum


A=Solution()
print(A.tribonacci(2))