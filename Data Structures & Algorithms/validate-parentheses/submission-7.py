# If my pointer is in a closing bracket the last bracket must be an open bracket

class Solution:
    closing_matches ={
    ")": "(",
    "}": "{",
    "]": "[",  
    }

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in self.closing_matches:
                if not stack:
                    return False
                    
                correspoding_braket = stack.pop()

                if self.closing_matches[char] != correspoding_braket:
                    return False
            else:
                stack.append(char)
                
        return True if not stack else False
