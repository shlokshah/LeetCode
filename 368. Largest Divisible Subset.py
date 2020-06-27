class Solution:
    def largestDivisibleSubset(self, nums):
        n=len(nums)
        if n==0:
            return
        if n==1:
            return nums
        count=[1]*n
        nums=sorted((nums))
        for i in range(n):
            for j in range(i-1,-1,-1):
                if nums[i]%nums[j]==0:
                    count[i]=max(count[i],count[j]+1)

        maxIndex=0
        for i in range(n):
            if count[i]>count[maxIndex]:
                maxIndex=i

        result=[]
        temp=nums[maxIndex]
        currentCount=count[maxIndex]
        for i in range(maxIndex, -1, -1):
            if temp%nums[i]==0 and currentCount==count[i]:
                result.append(nums[i])
                temp=nums[i]
                currentCount-=1
        return result


A=Solution()
print(A.largestDivisibleSubset([1,2,4,8]))
