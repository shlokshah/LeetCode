class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c=i=j=0
        s=m+n
        temp=[]
        while c<s:
            if i<m and j<n:
                if nums1[i]<nums2[j]:
                    temp.append(nums1[i])
                    i+=1
                    c+=1
                else:
                    temp.append(nums2[j])
                    j+=1
                    c+=1
            else:
                if i<m:
                    temp.append(nums1[i])
                    i += 1
                    c += 1
                else:
                    temp.append(nums2[j])
                    j += 1
                    c += 1
        nums1=temp
        print(nums1)





A=Solution()
A.merge([1,4,6,8,0,0,0],4, [3,5,9], 3)