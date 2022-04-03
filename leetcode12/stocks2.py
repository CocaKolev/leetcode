from typing import List
import statistics
class Solution:
    def maxProfit(prices: List[int]) -> int:

        if len(prices)<=1:
             return 0

        currentBeginningIndex=findStart(prices)
        
        
        if currentBeginningIndex==len(prices)-1:
            return 0

        minPrice,profit,index=prices[currentBeginningIndex], 0,currentBeginningIndex

        for x in range(currentBeginningIndex,len(prices)):
            if x>minPrice:
                profit=profit+prices[x]-minPrice
                minPrice=findMin(prices[index:])
                x=x+findStart(prices[index:])
            index+=1
            

        return profit

def findStart(currentListOfPrice):
    beginningPoint=0
    for x in range(0,len(currentListOfPrice)-1):
            if currentListOfPrice[x]<currentListOfPrice[x+1]:
                beginningPoint=x
                break
    return beginningPoint

def findMin(currentListOfPrice):
    beginningPoint=0
    for x in range(0,len(currentListOfPrice)-1):
            if currentListOfPrice[x]<currentListOfPrice[x+1]:
                beginningPoint=x
                break
    return currentListOfPrice[beginningPoint]


#print(Solution.maxProfit([1,2,3,4,5]))

print(Solution.maxProfit([3,2,6,5,0,3]))

print(Solution.maxProfit([7,1,5,3,6,4]))

print(Solution.maxProfit([7,6,4,3,1]))



# newPrices=[]
#         counterBegin,counterEnd, lows, highs=0,prices[(len(prices)-2)],0,0
#         if len(prices)<=1:
#             return 0

#         for x in range(0,len(prices)-1):
#             if prices[x]<prices[x+1]:
#                 counterBegin=x
#                 break
        
#         # for x in range(len(prices)-2, counterBegin, -1):
#         #     if prices[x+1]>prices[x] & prices[x]>prices[x-1]:
#         #         counterEnd=x
        
#         for x in range(counterBegin, counterEnd+1):
#             newPrices.append(prices[x])

#         medianPrice=statistics.median(newPrices)

#         for x in newPrices:
#             if x<medianPrice:
#                 lows+=x
#             if x>medianPrice:
#                 highs+=x
        
#         return highs-lows