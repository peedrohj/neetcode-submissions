class Solution:
    """
    [2,1,5,1,5,3]
     ||


    target = 3
    
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total_value = 0,0
        length = None

        for right in range(len(nums)):
            total_value += nums[right]

            while total_value >= target:
                if length is None:
                    length = (right - left) + 1 

                length = min((right - left) + 1, length)
                total_value -= nums[left]
                
                left += 1

        return length if length else 0