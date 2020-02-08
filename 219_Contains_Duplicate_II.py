from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Try using two pointer (Too Slow)
        """
        #  for i in range(len(nums) - 1):
        #      for j in range(i+1, i+k+1):
        #          if j == len(nums):
        #              break
        #          if nums[i] == nums[j]:
        #              return True
        #  return False

        numsDict = {}

        for index in range(len(nums)):
            if nums[index] not in numsDict:
                numsDict[nums[index]] = index
            else:
                if index - numsDict[nums[index]] <= k:
                    return True
                numsDict[nums[index]] = index

        return False


if __name__ == '__main__':
    test = Solution()
    print(test.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
    print(test.containsNearbyDuplicate([1, 0, 1, 1], 1))
