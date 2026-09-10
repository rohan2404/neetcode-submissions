class Solution:
    def isPalindrome(self, s: str) -> bool:
        z = "".join(s.split(" "))
        print(z)    
        L = 0
        R = len(s) - 1
        while L < R:
            l = s[L]
            r = s[R]
            if not l.isalnum():
                L += 1
                continue
            if not r.isalnum():
                R -= 1
                continue
            if l.lower() != r.lower():
                return False
            L+=1
            R-=1
        
        return True