class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_size = 0
        result_arr = []

        for i in nums:
            if i == 1:
                max_size += 1
            if i == 0:
                result_arr.append(max_size)
                max_size = 0

        result_arr.append(max_size)
        result = sorted(result_arr)[-1]

        return result