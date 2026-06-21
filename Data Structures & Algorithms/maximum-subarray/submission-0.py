class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        max_l, max_r = 0, 0
        left = 0

        for right in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
                left = right

            curr_sum = curr_sum + nums[right]

            if curr_sum > max_sum:
                max_sum = curr_sum
                max_l = left
                max_r = right

        return max_sum