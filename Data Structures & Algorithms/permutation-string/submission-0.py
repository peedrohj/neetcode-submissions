"""

Create an algorithm that can compare if a permutation of s1 is present in s2 
Input: s1 = "abc"_SR, , s2 = "lecabee"
Output: true

Requirements:
- Both strings contains lowercase letters.
- if a permutation of s1 exists as a substring of s2, then return true.


Solution
- Create a rolling window with the same size of s1 
- Compare the s1 with the window substring
- To verify permutations, sort both the substring and s1


"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        window = len(s1)
        start = 0

        while (start + window) <= len(s2):
            end = start + window

            if sorted(s2[start: end]) == s1:
                return True

            start += 1


        return False