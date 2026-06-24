class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        need = Counter(t)
        missing = len(t)

        left = start = end = 0

        for right in range(len(s)):
            if need[s[right]] > 0:
                missing -= 1
            need[s[right]] -= 1

            # When all characters are found
            while missing == 0:
                # Update result
                if end == 0 or right - left + 1 < end - start:
                    start, end = left, right + 1

                # Try shrinking
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return s[start:end]
        