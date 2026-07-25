class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        L = -1
        curr = best = 0
        for R in range(len(nums)):
            if nums[R] == 0:
                L = R
            curr = R - L
            best = max(curr, best)
        return best