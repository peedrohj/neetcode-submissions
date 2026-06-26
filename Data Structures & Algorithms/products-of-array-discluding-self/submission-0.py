import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        print(math.prod([1,2]))
        result = []

        for index in range(len(nums)):
            first_half = []
            second_half = nums[index+1:]

            if index > 0:
                first_half = nums[0:index]

            result.append(math.prod(first_half+second_half))

        return result