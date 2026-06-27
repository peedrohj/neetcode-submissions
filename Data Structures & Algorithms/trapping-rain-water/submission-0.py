"""

Create an algorithm that can return the maximum area of 
water that can be trapped between the bars.
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9

Requirements:
- The array have non-negative integers
- Each value height[i] represents the height of a bar
- Each bar has a width of 1

[3,1,0,1,3]
|


Solution:
- Get the highest one of both sides  
- Get the min value 
- the ammount of water that can be trapped
  min(right, left) - height[i]

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0

        for index in range(len(height)):
            if index == 0:
                continue
                
            ammount_of_water = min(max(height[0:index]), max(height[index:])) - height[index]

            if ammount_of_water <= 0:
                continue

            trapped_water += ammount_of_water


        return trapped_water