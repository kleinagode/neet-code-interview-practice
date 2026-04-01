class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hshMap = {}

        for i, number in enumerate(nums):
            nextNumber = target - number

            if nextNumber in hshMap.keys():
                return [hshMap[nextNumber], i]

            hshMap[number] = i

        return []