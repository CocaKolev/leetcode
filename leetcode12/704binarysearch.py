from typing import List

class Solution:
    def search(nums: List[int], target: int) -> int:

        minN,maxN=0,len(nums)
        midP=int((maxN/2))

        for x in range(0,len(nums)):
            if (target==nums[midP]):
                return midP
            elif (target<nums[midP]):
                maxN=midP
                midP=int((minN+maxN)/2)

            else:
                minN=midP
                midP=int((minN+maxN)/2)


        return -1

print(Solution.search([-1,0,3,5,9,12],2))