class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        res = []

        # Dict structure number: frequency

        for num in nums:
            seen[num] += 1

        max_heap = [(-value, key) for key, value in seen.items()]
        heapq.heapify(max_heap)

        for i in range(k):
            largest = heapq.heappop(max_heap)
            res.append(largest[1])

        return res