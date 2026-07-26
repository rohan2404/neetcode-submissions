class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for idx,string in enumerate(strs):
            for i,s in enumerate(string):
                num = ord(s)
                res += str(num)
                if i < len(string) - 1:
                    res += "_"
            res += "#"
        return res
    def decode(self, s: str) -> List[str]:
        def convert(string: str) -> str:
            res = ""
            sep = string.split("_")
            for x in sep:
                if x:
                    ascii_code = int(x)
                    res += chr(ascii_code)
            return res
        different_strings = s.split("#")
        different_strings.pop()
        out = []
        for code in different_strings:
            out.append(convert(code))
        return out