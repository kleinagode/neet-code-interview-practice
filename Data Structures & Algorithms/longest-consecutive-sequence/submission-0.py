class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Use a minheap to sort the elements O(n)
        if not nums:
            return 0

        heapq.heapify(nums)
        prev = heapq.heappop(nums)
        longest = 1
        current = 1

        while nums:
            num = heapq.heappop(nums)

            if num == prev:
                continue
            elif num == prev + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

            prev = num

        return max(longest, current)
