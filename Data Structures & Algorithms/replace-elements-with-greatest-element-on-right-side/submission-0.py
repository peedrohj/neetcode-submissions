class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        result_arr = [0] * len(arr)
        max_value = -1 

        for i in range(len(arr) -1, -1, -1):
            result_arr[i] = max_value
            max_value = max(arr[i], max_value)
        
        return result_arr