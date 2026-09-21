class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numbers = set(nums)
        seen = set()
        for x in numbers:
            if x-1 in numbers:
                seen.add(x)
            
        sequence_starts = numbers - seen
        best = 1
        for ss in sequence_starts:
            curr = 1
            x = ss
            while x+1 in numbers:
                curr += 1
                x += 1
                best = max(best, curr)
            
        return best