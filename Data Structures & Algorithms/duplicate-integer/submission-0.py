class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numsSet = set(nums)

        if len(nums) != len(numsSet):
            # a number appears more than once
            return True
        else:
            return False
