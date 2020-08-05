from typing import List


class Solution:

    #  def maxSubArray(self, nums: List[int]) -> int:
    #      # Dynamic Programming
    #      if len(nums) == 1:
    #          return nums[0]
    #      left = nums[-1]
    #      biggest = left
    #      for index in reversed(range(len(nums) - 1)):
    #          left = max(nums[index], nums[index] + left)
    #          biggest = max(biggest, left)

    #      return biggest

    def maxSubArray(self, nums: List[int]) -> int:
        biggest = -float("inf")
        val = -float("inf")
        for item in nums:
            if val + item < item:
                val = item
            else:
                val = item + val
            if biggest < val:
                biggest = val
        return biggest


if __name__ == "__main__":
    test = Solution()
    print(test.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(test.maxSubArray([-1, -2]))
