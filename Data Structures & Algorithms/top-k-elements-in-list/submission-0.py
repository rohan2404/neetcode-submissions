class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cts = Counter(nums)
        srt_cts = sorted(cts, key=cts.get, reverse=True)
        return srt_cts[:k]