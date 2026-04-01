class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sol = []

        for i in range(len(nums)):
            j = i + 1
            for j in range(j,len(nums)):
                if nums[i] + nums[j] == target:
                    sol.append(i)
                    sol.append(j)
                    return sol

        return sol