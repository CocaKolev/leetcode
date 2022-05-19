import time
from typing import List

start_time = time.time()


class Solution:
    # Solve with brute force for memory efficiency
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(0, len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return x, y

        return

    # Solve with Hash for speed efficiency
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for index, value in enumerate(nums):
            secondNum = target - nums[index]
            if secondNum in new_dict:
                return index, new_dict[secondNum]
            new_dict[value] = index
        return

        # USES FOR RANGE LOOP
        # new_dict = {}
        # for x in range(len(nums)):
        #     secondNum = target - nums[x]
        #     if secondNum in new_dict:
        #         return x, new_dict[secondNum]
        #     new_dict[nums[x]] = x

        # return


print(Solution.twoSum2(Solution, [3, 2, 4], 6))
print(Solution.twoSum2(Solution, [2, 7, 11, 15], 9))
print(Solution.twoSum2(Solution, [3, 3], 6))

print("Done %s seconds" % (time.time() - start_time))
