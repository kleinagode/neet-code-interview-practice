class Solution:
    # Optimal Solution using a hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hshMap = {}

        for i in range(len(nums)):
            number = nums[i]
            index = i
            nextNumber = target - number

            if nextNumber in hshMap.keys() and len(hshMap.keys()) != 0:
                return [hshMap[nextNumber], index]
            else:
                hshMap[number] = index
        return []
