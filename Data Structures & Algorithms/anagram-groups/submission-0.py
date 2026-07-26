from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s].append(s)
        out = []
        for _, ls in anagrams.items():
            out.append(ls)

        print(out)
        return out      