class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # In case k is larger than the array size

    # Reverse the entire array
        nums.reverse()

    # Reverse the first k elements
        nums[:k] = reversed(nums[:k])

    # Reverse the remaining n - k elements
        nums[k:] = reversed(nums[k:])

        return nums