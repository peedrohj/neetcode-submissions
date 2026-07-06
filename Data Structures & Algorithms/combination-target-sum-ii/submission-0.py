"""

Create an algorithm that given a list of integers, return all possible combinations that sum up
to the target value.

Input: candidates = [9,2,2,4,6,1,5], target = 8
Output: [
  [1,2,5],
  [2,2,4],
  [2,6]
]


Requirements:
- The list may contain duplicate values
- Each element may be chosen at most once.
- The solution set must not contain duplicate combinations.
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(index: int, curr: List[int]):

            curr_sum = sum(curr)

            if curr_sum == target:
                result.append(curr.copy())
                return

            if curr_sum > target or index >= len(candidates):
                return
            
            curr.append(candidates[index])
            dfs(index+1, curr)
            curr.pop()

            # Skip duplicate candidates for the current position
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            
            # Do not include the current candidate (or its duplicates)
            dfs(index+1, curr)


        dfs(0, [])

        return result
