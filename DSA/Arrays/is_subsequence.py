class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0 
        r = 0 
        while l < len(t) and r < len(s):
            if t[l] == s[r]:
                r += 1
            l += 1

        return r == len(s)
            
