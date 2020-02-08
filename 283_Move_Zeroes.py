from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        using array rotation in reversed method
        """
        #  def reverse(nums):
        #      start = 0
        #      end = len(nums) - 1
        #      while end > start:
        #          nums[end], nums[start] = nums[start], nums[end]
        #          start += 1
        #          end -= 1
        #      return nums

        #  count = 0
        #  previous = None
        #  for index in range(len(nums)):
        #      if nums[index] == 0:
        #          count += 1
        #          if count == 1:
        #              previous = index
        #              continue

        #          tmp = reverse(nums[previous:index])
        #          tmp[0:len(tmp)-count+1] = reverse(tmp[0:len(tmp)-count+1])
        #          nums[previous:index] = tmp
        #          previous = index - count + 1
        #  if previous is not None and nums[previous] == 0 and count > 0:
        #      tmp = reverse(nums[previous:index+1])
        #      tmp[0:len(tmp)-count] = reverse(tmp[0:len(tmp)-count])
        #      nums[previous:index+1] = tmp
        """
        Try to be fast using two pointer
        """
        count = 0
        for index in range(len(nums)):
            value = nums[index]
            if value == 0:
                count += 1
                continue
            if count and value:
                nums[index-count] = value
        index = len(nums) - 1
        for i in range(count):
            nums[index - i] = 0

        print(nums)


if __name__ == '__main__':
    test = Solution()
    test.moveZeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0])
