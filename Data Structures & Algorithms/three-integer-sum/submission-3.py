"""

Create an algorithm that can group three numbers that sums to zero
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Requirements:
- nums[i] + nums[j] + nums[k] == 0
- output should not contain any duplicate triplets
- return the output and the triplets in any order

Solution:
- Create a two sum algorithm and use the nums[i] as the target.
- (nums[j] + nums[k]) = nums[i]
- Interate trough the array and for each index call the two sum function
- create a set to store all triplets

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        start, end = 0, len(nums) - 1
        sumed_values = []

        while start < end:
            curr_sum = nums[start] + nums[end]

            if curr_sum == target:
                sumed_values.append([start, end])
                end -= 1
                start += 1

            if curr_sum > target:
                end -= 1

            if curr_sum < target:
                start += 1

        return sumed_values

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums = sorted(nums)

        for curr_index in range(len(nums)):
            two_sum = self.twoSum(nums=nums, target=(nums[curr_index] * -1))
            if len(two_sum) == 0:
                continue

            for start, end in two_sum:
                if start == curr_index or end == curr_index:
                    continue

                result = sorted([nums[curr_index], nums[start], nums[end]])
                triplets.add((tuple(result)))

        return list(triplets)
