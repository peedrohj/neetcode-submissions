"""

Create an algoritm that can get all possible subsets of a list.
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Requirements:
- The result must not contain any duplicates
- The subset are all integers

Solution: Create a decision tree algoritm that for each num creates a subset
with the current number and another one without the curent number

1 - [1], []
2 - [1, 2], [2]
3 - [1, 2, 3], [2,3], [3]

"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr_subset = [] 
        result = []

        def dfs(i):
            if i >= len(nums):
                result.append(curr_subset.copy())
                return

            curr_subset.append(nums[i])
            dfs(i+1)
            
            curr_subset.pop()
            dfs(i+1)


        dfs(0)

        return result
