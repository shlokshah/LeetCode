class Solution:
    def searchInsert(self, nums, target):
        try:
            a=nums.index((target))
            return a
        except ValueError:
            n=len(nums)
            if target<nums[0]:
                return 0
            elif target>nums[-1]:
                return n
            else:
                for i in range(n):
                    if target<nums[i+1] and target>nums[i]:
                        return i+1

A=Solution()
print(A.searchInsert([1,2,10,30],7))