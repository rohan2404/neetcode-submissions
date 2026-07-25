from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for idx, num in enumerate(nums):
            if (target-num) in seen:
                return [seen[target-num], idx]
            seen[num] = idx

        return