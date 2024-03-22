
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        count = 1  # Count of current element
        j = 1      # Index to place next non-duplicate element
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1  # Reset count for new element
            
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        
        return j
