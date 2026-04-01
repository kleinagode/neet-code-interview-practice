class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        tCopy = [x for x in t]

        # Have to be the same length
        if len(s) == len(t):

            # Each char in the s has to be in t
            for char in s:
                if char not in tCopy:
                    return False
                else:
                     tCopy.remove(char)

            # If all conditions apply it is an anagram
            return True
        else:
            return False
        