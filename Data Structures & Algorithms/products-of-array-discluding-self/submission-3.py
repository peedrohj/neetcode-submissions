import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {}
        postfix = {}
        result = []

        for index in range(len(nums)):
            if index == 0:
                prefix[index] = nums[index]
                continue

            prefix[index] = prefix[index -1] * nums[index]


        for index in range(len(nums) - 1, -1, -1):
            if index == len(nums) - 1:
                postfix[index] = nums[index]
                continue

            postfix[index] = postfix[index + 1] * nums[index]


        print(f"Prefix: {prefix}")
        print(f"postfix: {postfix}")
        
        for index in range(len(nums)):
            start = prefix[index -1] if index > 0 else 1
            end = postfix[index + 1] if index < len(nums) -1 else 1
            result.append(start * end)

        return result