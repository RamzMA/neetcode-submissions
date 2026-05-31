class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True

        i = 0
        for letter in t:
            if i == len(s):
                break
            if letter == s[i]:
                i+=1
        return len(s) == i
        