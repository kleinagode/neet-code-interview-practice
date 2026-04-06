
class Solution:

    def encode(self, strs):
        msg = ""
        for s in strs:
            msg += str(len(s)) + "$" + s

        return msg

    def decode(self, s):
        
        res = []

        i = 0
        for ch in s:

            while i < len(s):
                j = i
                while s[j] != "$":
                    j += 1
                length = int(s[i:j])
                res.append(s[j+1 : j + 1 + length])
                i = j + 1 + length  

        return res






