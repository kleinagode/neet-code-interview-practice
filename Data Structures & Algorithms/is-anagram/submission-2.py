class Solution:

    # Optimized solution using a hashmap
    def isAnagram(self, s: str, t: str) -> bool:

        hashA = {}
        hashB = {}
        if len(s) == len(t):
            for letter in s:
                hashA[letter] = s.count(letter)
            for letter in t:
                hashB[letter] = t.count(letter)

            for entry in hashA:
                if entry in hashB:
                    if hashA[entry] != hashB[entry] :
                        return False
                else:
                    return False
            return True

        else:
            return False
        