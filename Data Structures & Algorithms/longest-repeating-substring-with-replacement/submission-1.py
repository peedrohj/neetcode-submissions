class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0 
        start, end = 0, 0
        counter = {}

        while end < len(s):
            if s[end] in counter:
                counter[s[end]] += 1
            else:
                counter[s[end]] = 1

            # Calculate length of window - count of most frequent character
            print(f"counter.values(): {max(counter.values())} | {counter.values()}")
            while (end - start + 1) - max(counter.values()) > k:
                counter[s[start]] -= 1
                start += 1
            
            result = max(result, (end - start) + 1)
            end += 1

        return result