from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic, t_dic = Counter(s), Counter(t)
        return (s_dic == t_dic)