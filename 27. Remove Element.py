'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        i=0
        n=len(nums)
        for j in range(n):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i

A=Solution()
print(A.removeElement([2,3,3],2))
