class Solution:
    def getDescentPeriods(self,prices):
        count=1
        total=1
        for i in range(1,len(prices)):
            if prices[i]==prices [i-1]-1:
                count+=1
            else:
                count=1
            total +=count
        return total              