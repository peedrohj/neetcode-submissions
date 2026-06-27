"""

Create an algorithm that can check if a string is a palindrome.
Requirements:
- palindrome is string that reads the same forward and backward
- case-insensitive
- ignore non-alphanumeric characters 

Input: "Was it a car or a cat I saw?"
Output: True

Solution:
- Create a pointer at start 
- Create a pointer at the end 
- Ignore all non-alphanumeric characters
- The values of those two pointers must be equal 

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", '').lower()

        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and not s[start].isalnum():
                start += 1

            while end > start and not s[end].isalnum():
                end -= 1

            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True 