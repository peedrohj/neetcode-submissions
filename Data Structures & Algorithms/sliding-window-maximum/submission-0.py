class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        start = 0
        while start + k < len(nums) + 1:
            sub = nums[start: start + k]
            result.append(max(sub))
            start += 1

        return result