class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        if len(A)==1:
            return A
        b_s=sorted(B)
        a_s=sorted(A)
        b=[]
        a=[]
        while len(a_s)>0:
            if b_s[0]<a_s[0]:
                b.append(b_s.pop(0))
                a.append(a_s.pop(0))
            else:
                b.append(b_s.pop(len(b_s)-1))
                a.append(a_s.pop(0))
        result=[]
        for i in B:
            idx=b.index(i)
            result.append(a[idx])
            a.pop(idx)
            b.remove(i)
        return result