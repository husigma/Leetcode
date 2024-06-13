from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = []

        for i in range(len(nums)):
            for h in range(i):
                if nums[i]+ nums[h] == target:
                    j.append(i)
                    j.append(h)
                else:
                    continue

        return j