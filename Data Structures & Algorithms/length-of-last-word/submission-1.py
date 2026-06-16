class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        s = s.strip()
        right = len(s)-1

        while s[right].isalpha() and s[right] != ' ' and right >= 0:
            res+=1
            right-=1
        return res



        