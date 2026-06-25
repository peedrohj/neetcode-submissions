"""

The objective is to group all anagrams from a given array.

Input: ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Break down:
- Indentify anagrams
- Go trough the list and store all anagrams.
- Check if the anagram is alredy stored, if not, save it. 

def is_anagram(string1: str, string2: str) -> bool:
    return sorted(string1) == sorted(string2)

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for string in strs:
            curr_str = "".join(sorted(string))
            hashmap[curr_str] = hashmap.get(curr_str, []) + [string]
        
        return list(hashmap.values())