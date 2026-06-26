"""

Given an array of number returns the most frequent elements

Requirements:
- Return the top "k" elements
- The answer is always unique
- Return the output in any order

Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

---

- Go trough the array
- Store the value and a counter
- Increment the counter each time a number appears
    - Check if this has been counted before
    - If not initialize the data if a default value of "1"

HashMap: Search O(1)
- Sort the hasmap using the counter as the key
- Return the hasmap top "k" elements

"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        
        for number in nums:
            hashmap[str(number)] = 1 + hashmap.get(str(number), 0)

        sorted_hash = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))


        cnt = 0
        store = []
        for key,val in sorted_hash.items():
            if cnt < k:
                store.append(key)
            cnt += 1    
        
        return store
