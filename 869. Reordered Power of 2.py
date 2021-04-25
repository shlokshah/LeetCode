class Solution:
    def makelist(self, N):
        t = []
        while N!=0:
            t.append(N%10)
            N=N/10
        t=t.sort(reverse=True)
        return t

    def reorderedPowerOf2(self, N: int) -> bool:
        map={}
        for i in range(30):
            map[i]=self.makelist(2**i)
        N_list=self.makelist(N)
        if N_list in map.values():
            return True
        else:
            return False

if __name__ == '__main__':
    A=Solution()
    print(A.reorderedPowerOf2(41))
