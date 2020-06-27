class Solution:
    def defangIPaddr(self, address: str) -> str:
        address=address.replace(".","[.]")
        return address

A=Solution()
print(A.defangIPaddr("2.5.6"))