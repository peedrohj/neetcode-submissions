"""

Create an algorithm that can return the area a square from a
array of heights with a given index and value. 
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Requirements:
- Choose any two bars to form a container
- Amount of water = Area of the container
- Return the maximum area

Solution:
- Use a two pointers Solution
- For each index, calculate the area for every elemente in array 
- Store the value of the max area



"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for start in range(len(heights)):
            end = len(heights) - 1

            while end > start:
                length = min(heights[start], heights[end])
                width = end-start 

                max_area = max(length * width, max_area)

                end -= 1


        return max_area