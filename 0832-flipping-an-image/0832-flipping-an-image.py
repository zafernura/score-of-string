from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            
            while left <= right:
                # If both are same, invert them
                if row[left] == row[right]:
                    row[left] ^= 1
                    if left != right:
                        row[right] ^= 1
                
                # Move pointers
                left += 1
                right -= 1
        
        return image