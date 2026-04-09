class Solution:
    def threeSum(self, nums):
        numsSorted = sorted(nums)
        res = []

        for idx, num in enumerate(numsSorted):

            if idx > 0 and num == numsSorted[idx - 1]:
                continue

            l, r = idx + 1, len(numsSorted) - 1

            while l < r:
                total = num + numsSorted[l] + numsSorted[r]

                if total > 0:
                    r -= 1

                elif total < 0:
                    l += 1

                else:
                    res.append([num, numsSorted[l], numsSorted[r]])

                    l += 1

                    # skip duplicates for l
                    while l < r and numsSorted[l] == numsSorted[l - 1]:
                        l += 1

                    # optional but recommended: skip duplicates for r
                    r -= 1
                    while l < r and numsSorted[r] == numsSorted[r + 1]:
                        r -= 1

        return res