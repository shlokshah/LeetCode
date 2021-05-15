# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        n1 = rand7()
        n2 = rand7()
        while (n1 > 5):
            n1 = rand7()
        while n2 == 7:
            n2 = rand7()
        if 4 <= n2 <= 6:
            return n1 + 5
        else:
            return n1
