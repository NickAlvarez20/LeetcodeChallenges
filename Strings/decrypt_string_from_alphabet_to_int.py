class Solution:
    def freqAlphabets(self, s: str) -> str:
        a_i_dict = {}
        j_z_dict = {}
        res = ""
        for i in range(1,10):
            a_i_dict[str(i)] = chr(ord("a")+i-1)
        for i in range(10, 27):
            j_z_dict[f"{i}#"] = chr(ord("a")+i-1)
        i = 0
        while i < len(s):
            if i+2 < len(s) and s[i+2] == "#":
                new_slice = s[i:i+3]
                res += j_z_dict[new_slice]
                i += 3
            else:
                res += a_i_dict[s[i]]
                i += 1
        return res


        