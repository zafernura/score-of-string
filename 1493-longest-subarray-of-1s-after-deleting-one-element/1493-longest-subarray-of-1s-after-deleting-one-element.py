class Solution:
    def longestSubarray(self, nums):
        groups=[]
        count=0
        for num in nums:
            if num==1: 
                 count += 1
            else:
                groups.append(count)
                count = 0
        groups.append(count)
        ans = 0
        for i in range(len(groups) - 1):
            ans = max(ans, groups[i] + groups[i+1])
        if 0 not in nums:
           return  len(nums) - 1
        return ans
        