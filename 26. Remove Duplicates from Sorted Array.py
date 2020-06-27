class Solution:
    def removeDuplicates(self, nums) -> int:
        j=1
        if len(nums)==0:
            return 0
        else:
            for i in range(1,len(nums)):
                if nums[i]!=nums[i-1]:
                    nums[j]=nums[i]
                    j+=1
            return j




A=Solution()
print(A.removeDuplicates([1,2]))