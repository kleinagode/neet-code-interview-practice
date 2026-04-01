class Solution:
    def areAnagram(self, word1: str, word2: str):
        letterMap1 = {}
        letterMap2 = {}

        if len(word1) != len(word2):
            return False

        for i in range(len(word1)):
            letter1 = word1[i]
            letter2 = word2[i]

            if letter1 not in letterMap1:
                letterMap1[letter1] = word1.count(letter1)

            if letter2 not in letterMap2:
                letterMap2[letter2] = word2.count(letter2)

        for letter in letterMap1:
            if letterMap1[letter] != letterMap2.get(letter, 0):
                return False

        return True

    from typing import List

class Solution:
    def areAnagram(self, word1: str, word2: str):
        letterMap1 = {}
        letterMap2 = {}

        if len(word1) != len(word2):
            return False

        for i in range(len(word1)):
            letter1 = word1[i]
            letter2 = word2[i]

            if letter1 not in letterMap1:
                letterMap1[letter1] = word1.count(letter1)

            if letter2 not in letterMap2:
                letterMap2[letter2] = word2.count(letter2)

        for letter in letterMap1:
            if letterMap1[letter] != letterMap2.get(letter, 0):
                return False

        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        used = set()   # now stores indices, not words

        for i in range(len(strs)):
            if i in used:
                continue

            curWord = strs[i]
            anagramMap[i] = [curWord]   # use index as key
            used.add(i)

            for j in range(i + 1, len(strs)):
                if j not in used and self.areAnagram(curWord, strs[j]):
                    anagramMap[i].append(strs[j])
                    used.add(j)

        return list(anagramMap.values())