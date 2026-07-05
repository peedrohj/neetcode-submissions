"""

Create an algorithm that given a list of numbers can return all the possible combinations 
that sum to the target value

Input: nums = [2,5,6,9], target = 9
Output: [[2,2,5],[9]]

Requiremets:
- We can return the combinations any order
- We can return the numbers any order
- We can the same index multiple times

Solution:
- For each index create a decision tree where we add the value till we reach out the target 
and another path where we dont add the value and go to the next index.
                                        
                            [2]           
                [2, 2]              [2,5]    
        [2, 2, 2]     [2, 2, 5]             [2, 5, 5]
[2, 2, 2, 2]              |

- Use a dfs algorithm to go deep as possible in the decision and tree and if it sums to the target
value add it to the result list.

"""


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index, curr_list):
            current_sum = sum(curr_list)

            if current_sum == target:
                result.append(curr_list.copy())
                return

            if index >= len(nums) or current_sum > target:
                return


            dfs(index + 1, curr_list=curr_list.copy())
            curr_list.append(nums[index])
            dfs(index, curr_list=curr_list.copy())


        dfs(0, [])
        return result
        