
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)

        # gcd
        while l2:
            l1, l2 = l2, l1%l2

        gcd = l1

        s = str1[:l1]
        x = int(len(str1)/gcd)
        y = int(len(str2)/gcd)
        

        if s*x == str1 and s*y == str2:
            return s
        
        s = ""
        return s 


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd = math.gcd(len(str1),len(str2))
        return str1[:gcd]
