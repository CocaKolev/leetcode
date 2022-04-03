from typing import List
class Solution:
    def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k>len(nums):
            k=k%len(nums)
        x,y=0,k

        if len(nums)>1:
            new=[0]*len(nums)
            for x in range(0,len(nums)):
                y=x+k
                if y>=len(nums):
                    y=y-len(nums)
                new[y]=nums[x]

            for x in range(0,len(nums)):
                nums[x]=new[x]
        return nums
print(Solution.rotate([1,2],3))


# def rotate(nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         x,y=0,0
#         # if k != 1 :
#         while(x<k):
#             a,b=nums[0],0
#             for y in range(1,len(nums)):
#                 if y<len(nums):
#                     b=nums[y]
#                     nums[y]=a
#                     a=b
                
#             b=nums[y]
#             nums[0]=a
#             b=a
#             x+=1

#         return nums