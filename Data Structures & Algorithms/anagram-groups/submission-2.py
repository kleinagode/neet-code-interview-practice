class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Mapping the letters to positions in the array, hashmap would be better but a hashmap
        # cannot be a key to another hashmap because it has to be immutable. I know I can use 
        # ASCII values but it is too complicated and unneccesary for me to understand

        alpha_map = {
            'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
            'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
            'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
            'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
            'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
            'z': 25
        }

        res = defaultdict(list)

        for word in strs:
            # Init the array with zeroes
            count = [0] * 26   

            for letter in word:
                # Making a universal key for the res hashmap
                count[alpha_map[letter]] += 1  
            # Has to be a tuple because python dict keys have to be immutable and tuples are
            res[tuple(count)].append(word)

        return list(res.values())