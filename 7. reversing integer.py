class Solution:
    def reverse(self, x: int) -> int:
        if x >= (2**31)-1 or x <= -(2**31):
            return 0
        else:
            if x < 0:
                sign = -1
                a = (-1) * x
            else:
                sign = 1
                a = x
            r = 0
            while a != 0:
                r = r * 10
                r = r + (a % 10)
                a //= 10

            if r >= 2147483647 or r <= -2147483648:
                return 0
            if sign == -1:
                r = 0 - r
                return r
            else:
                return r


A=Solution()
print(type(A.reverse(1534236469)))

print(2**31)