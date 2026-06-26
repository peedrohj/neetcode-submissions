"""

Find longest consecutive sequence from a given array.
Input: [2,20,4,10,3,4,5]
Output: int: longest consecutive sequence

Requirements:
- O(n)
- element is exactly 1 greater than the previous one
- The elements do not have to be consecutive

Brute force Solution:
- Sort the array
- Interate trought the array with two pointers
- Start with the previous at zero and next at 1
- The next point must be exactly 1 greater than previous pointer
- Store the diff between those two pointers.

Example:
[1,2,9,8,6,7,8]

"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_number = set(nums)
        longest = 0

        for num in hash_number:
            previous = (num - 1)

            if previous not in hash_number:
                length = 1
                
                while (num + length) in hash_number:
                    length += 1
                    
                longest = max(length, longest)

        return longest
