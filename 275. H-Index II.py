class Solution:
    def hIndex(self, citations):
        length = len(citations)
        first = 0
        count = length
        while count > 0:
            step = int(count / 2)
            mid = first + step
            if citations[mid] < length - mid:
                first = mid + 1
                count -= (step + 1)
            else:
                count = step
        return length - first


A=Solution()
print(A.hIndex([0,1,3,5,6]))