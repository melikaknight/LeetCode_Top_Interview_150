
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        steps = 0
        max_reach = 0
        next_reach = 0
        
        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == next_reach:
                steps += 1
                next_reach = max_reach
                if next_reach >= n - 1:
                    break
        
        return steps
