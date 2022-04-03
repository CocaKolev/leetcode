from typing import List
class Solution:
    def sortedSquares(nums: List[int]) -> List[int]:
        nums2=[x*x for x in nums]
        nums2.sort()
        return nums2


print(Solution.sortedSquares([-4,-1,0,3,10]))