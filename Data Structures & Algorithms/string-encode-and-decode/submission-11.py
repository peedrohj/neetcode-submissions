"""

Create two functions to encode and decode data.
- The encode function should receive a list of strings and return a 
single string 

- The decode function should receive a string and return a list of strings.

Requirements:
- The string contains any ASCII characters 



"""
import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_word = str()

        for word in strs:
            encoded_word += f"{len(word)}#{word}"

        return encoded_word

    def decode(self, s: str) -> List[str]:
        words = []

        i = 0
        
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1


            length = int(s[i:j].strip())

            # Ignore the "#"
            j += 1
            words.append(s[j:j+length])
            i = j+length

        return words