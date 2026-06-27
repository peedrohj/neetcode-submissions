"""

from types import _ReturnT_co
Create an algorithm that can find the indexes of two numbers 
that the sum is equal to the target. 

Input: numbers = [1,2,3,4], target = 3
Output: [1,2]

Requirements:
- O(1) additional space
- To numbers is sorted in a increasing order
- The index cannot be equal 
- 1-indexed array 
- index1 < index 2
- Theres exactly one valid solution

Solution:
- Create two pointers start and end.
- If the sum of those two is less than the target increment the start pointer by 1 
- If not, decrease the end pointer by 1.
- Repeat until start is greather or equal the end 
- If the sum oh those two pointers match the target return [start + 1, end + 1]
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            diff = target - (numbers[start] + numbers[end]) 
            
            if diff == 0:
                return [start + 1, end + 1]

            if diff > 0:
                start += 1

            if diff < 0:
                end -= 1

        
        return []