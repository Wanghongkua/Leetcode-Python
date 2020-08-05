from typing import List


class Solution:
    """
    Hash Table
    """
    #  def twoSum(self, nums: List[int], target: int) -> List[int]:
    #      numsDict = {}
    #      for index in range(len(nums)):
    #          if nums[index] not in numsDict:
    #              numsDict[nums[index]] = []
    #          numsDict[nums[index]].append(index)
    #      for index in range(len(nums)):
    #          if target - nums[index] in numsDict:
    #              if nums[index] * 2 == target:
    #                  if len(numsDict[nums[index]]) == 1:
    #                      continue
    #                  return numsDict[nums[index]][:2]
    #              return [index, numsDict[target - nums[index]][0]]
    """
    One-Pass Hash Table
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for index in range(len(nums)):
            if target - nums[index] in numsDict:
                return [numsDict[target - nums[index]], index]
            if nums[index] not in numsDict:
                numsDict[nums[index]] = index


if __name__ == "__main__":
    test = Solution()
    print(test.twoSum([2, 7, 11, 15], 9))
