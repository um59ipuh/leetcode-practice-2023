from pytest import *

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #first aprch
        uniques = set()
        vacant = 0
        for index in range(len(nums)):
            # if present 
            if nums[index] in uniques:
                continue
            uniques.add(nums[index])
            nums[vacant] = nums[index]
            vacant += 1
            
        return vacant
    
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1: return 0
        max_profit = 0
        for first in range(len(prices)):
            for second in range(first + 1, len(prices)):
                profit = prices[second] - prices[first]
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit
                    
        
        
def test_program():
    sol = Solution()
    
    # Remove Duplicates from Sorted Array
    # assert sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
    # assert sol.removeDuplicates([0,1,1,1,1]) == 2
    
    assert sol.maxProfit([7,1,5,3,6,4]) == 7
    assert sol.maxProfit([1,2,3,4,5]) == 4
    assert sol.maxProfit([7,6,4,3,1]) == 0
        
if __name__ == "__main__":
    test_program()
