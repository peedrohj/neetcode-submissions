"""

Input: list_of_nums, target
Return: Two index that we can sum to get this target

Brute force: Loop the list_of_nums of i and j and return the first index 
where list_of_nums[i] + list_of_nums[j] = target. O(n²)


Clever: Create hashmap to store each numbers and index. 

list_of_nums[i] - target  =  list_of_nums[j]

If list_of_nums[j] exists in hashmap return the index. If not, store the current and the 
index in the hashmap

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index in range(len(nums)):
            diff = target - nums[index] 

            if diff in hashmap:
                return [hashmap[diff], index]

            if nums[index] not in hashmap:
                hashmap[nums[index]] = index
            
        return []