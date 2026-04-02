class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using bucket sort for O(n) time

        freqHashMap = defaultdict(int)

        # Step 1: Count frequencies
        for num in nums:
            freqHashMap[num] += 1

        # Step 2: Create buckets where index = frequency
        freqBucket = [[] for _ in range(len(nums) + 1)]

        # Step 3: Fill buckets
        for num, freq in freqHashMap.items():
            freqBucket[freq].append(num)

        # Step 4: Gather results from high freq to low
        res = []
        for i in range(len(nums), 0, -1):
            for num in freqBucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res
