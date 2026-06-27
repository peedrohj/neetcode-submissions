"""

Create an algorithm that given a list of temperatures can calculate how many
days is warmer than the current day. 

Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]

Requirements:
- The temperature is warmer if current day < next day.
- The default value is 0 

Solution:
- Use a stack to store all the temperatures and their index 
- If we find a temperature that is greather than the head of the stack 
- Pop the elemente and subtract their index 
- number of warmer days = current index - colder day index 


"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        queue = collections.deque()
        result = [0] * len(temperatures)

        for index in range(len(temperatures)):

            while queue and temperatures[index] > queue[-1][0]:
                _, cold_index = queue.pop()
                result[cold_index] = index - cold_index
        
            queue.append((temperatures[index], index))

        return result