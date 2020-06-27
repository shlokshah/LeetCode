class Solution:
    def isValid(self, s: str) -> bool:
        dict={'}':'{', ')':'(', ']':'['}
        lenth=-1
        stack=[]
        if len(s)==0:
            return True
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
                lenth=lenth+1
            try:
                if i in [')','}',']']:
                    if stack[lenth]!=dict[i]:
                        return False
                    else:
                        a=stack.pop()
                        lenth=lenth-1
            except:
                return False
        if lenth==-1:
            return True

A=Solution()
print(A.isValid("[]"))

'''
-------OPTIMAL-------
class Solution(object):
    def isValid(self, s):
        
        if len(s)%2!=0:
            return False
        opening = set('([{')
        matches = set([('(', ')'), ('[', ']'), ('{', '}')])
        stack = []
        
        for paren in s:
            if paren in opening:
                stack.append(paren)
            else:
                if len(stack)==0:
                    return False
                last_open = stack.pop()
                if (last_open, paren) not in  matches:
                    return False
        return len(stack)==0
'''