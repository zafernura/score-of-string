class Solution(object):
    def countDigitOccurrences(self, nums, digit):
      count=0

      for num in nums:
        for ch in str(num):
            if ch==str(digit):
                count+=1
      return count         
        