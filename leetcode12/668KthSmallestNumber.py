class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        #m is number of rows, n is number of columns
        if m==1 and n==1:
            return 1
        x,y=1,1
        nums=[]
        
        #iterate through columns 
        for x in range(1,n+1):
            #now iterate through every row in each column
            for y in range(1,m+1):
                nums.append(y*x)
                #stop going down the column when the product is more than the position you would want
                if (x*y)>k:
                    break
                
        nums.sort()
        
        return nums[k-1]


print(Solution.findKthNumber(Solution,7,11,71))
#print(Solution.findKthNumber(Solution,9895,28405,100787757))

# class Solution:
#     def findKthNumber(self, m: int, n: int, k: int) -> int:
#         if m==1 and n==1:
#             return 1

#         nums=[]
#         for x in range(1,m+1):
#             y=1
#             while x*y<=k and y<=n:
#                 nums.append(x*y)
#                 y+=1
#         nums.sort()
        
#         return nums[k-1]
