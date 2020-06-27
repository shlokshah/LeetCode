class Solution:
    def reconstructQueue(self, people):
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        l=[]
        for i in range(len(people)):
            l.insert(people[i][1], people[i])
        return l

A=Solution()
print(A.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
