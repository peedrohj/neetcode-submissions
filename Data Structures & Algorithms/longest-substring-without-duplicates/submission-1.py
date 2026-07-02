"""

Create an algorithm that can find the lenght of the longest substring.
Input: s = "zxyzxyz"
Output: 3

Requirements:
- Do not have any duplicated characters.

Solution:
- Sliding window problem
- A pointer at the start of the string 
- Interate with and end pointer
- A set with all characters found till now 
- If a char is in the set, begin = end.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        begin = 0
        end = 0 
        char = set()

        while end < len(s):
            if s[end] in char:
                result = max(result, end - begin)
                while s[end] in char:
                    char.remove(s[begin])
                    begin += 1

            char.add(s[end])
            end += 1

        return max(result, end - begin)
