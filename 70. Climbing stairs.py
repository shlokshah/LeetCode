class Solution:
    def climbStairs(self, n):
        a = b = 1
        # a -> current step
        # b-> ways to get to next step
        for _ in range(n):
            a, b = b, a + b
        return a

A=Solution()
print(A.climbStairs(4))

