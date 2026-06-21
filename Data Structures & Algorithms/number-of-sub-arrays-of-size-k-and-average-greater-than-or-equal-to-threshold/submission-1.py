class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        count = 0

        for right in range(k, len(arr) + 1):
            if right - left > k:
                left += 1

            if sum(arr[left:right]) / k >= threshold:
                count +=1

        return count