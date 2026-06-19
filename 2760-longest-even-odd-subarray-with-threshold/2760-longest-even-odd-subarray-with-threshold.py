class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        max_len = 0
        n = len(nums)
        
        for i in range(n):
            # start must be even and <= threshold
            if nums[i] % 2 != 0 or nums[i] > threshold:
                continue
            
            length = 1
            prev = nums[i]
            
            for j in range(i + 1, n):
                # check threshold and alternating condition
                if nums[j] > threshold or nums[j] % 2 == prev % 2:
                    break
                
                length += 1
                prev = nums[j]
            
            max_len = max(max_len, length)
        
        return max_len
        