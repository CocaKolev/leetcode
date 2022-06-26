from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        # BRUTE FORCE
        # volume = 0
        # for x in range(0, len(height)):
        #     for y in range(x, len(height)):
        #         if min(height[x], height[y]) * (y-x) > volume:
        #             volume = min(height[x], height[y]) * (y-x)

        # return volume

        leftWall = 0
        rightWall = len(height) - 1
        shortline = min(height[leftWall], height[rightWall])

        maxVolume = Solution.findVolume(height, leftWall, rightWall)
        while leftWall < rightWall:
            if height[leftWall] > height[rightWall]:
                rightWall -= 1
            elif height[leftWall] < height[rightWall]:
                leftWall += 1
            else:
                leftWall += 1

            tempVol = Solution.findVolume(height, leftWall, rightWall)
            if maxVolume < tempVol:
                maxVolume = tempVol

        return maxVolume

    def findVolume(height, left, right):
        return min(height[left], height[right]) * (right - left)


print(Solution.maxArea(Solution, [1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(Solution.maxArea(Solution, [1, 1]))
