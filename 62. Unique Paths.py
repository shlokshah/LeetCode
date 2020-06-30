class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 1
        dp=[[1 for x in range(n)] for x in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]

A=Solution()
print(A.uniquePaths(7,3))
