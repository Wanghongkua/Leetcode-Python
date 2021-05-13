from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Dynamic Programming
        """
        #  maximum = -float("inf")
        #  localMaximum = -float("inf")
        #  for index in range(len(nums)):
        #      if localMaximum + nums[index] < nums[index]:
        #          localMaximum = nums[index]
        #      else:
        #          localMaximum += nums[index]
        #      if localMaximum > maximum:
        #          maximum = localMaximum
        #  return maximum
        """
        Less code version of DP
        """
        localMaximum = maximum = nums[0]
        for index in range(1, len(nums)):
            localMaximum = max(localMaximum + nums[index], nums[index])
            maximum = max(localMaximum, maximum)
        return maximum


if __name__ == "__main__":
    test = Solution()
    print(test.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
