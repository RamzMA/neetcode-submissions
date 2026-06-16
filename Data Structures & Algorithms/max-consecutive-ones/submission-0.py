class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        m = 0

        for num in nums:
            if num == 1:
                res += 1
            else:
                res = 0
            m = max(m, res)
        return m
        