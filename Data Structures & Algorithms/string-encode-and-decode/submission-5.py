class Solution:

    def encode(self, strs: List[str]) -> str:
        res_str = ""
        self.size = []
        for s in strs:
            self.size.append(len(s))
            res_str += s
        return res_str


    def decode(self, s: str) -> List[str]:
        res_strs = []
        cs = [c for c in s]
        for c in cs:
            if c == "":
                cs.remove(c)

        for i in range(len(self.size)):
            s = ""
            for c in cs[:self.size[i]]:
                s += c
                cs.remove(c)
            res_strs.append(s)
        return res_strs
                
