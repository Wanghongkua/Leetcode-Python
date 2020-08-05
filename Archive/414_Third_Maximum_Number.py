from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        Scan list for 3 times
        """
        #  maximum = nums[0]
        #  for index in range(1, len(nums)):
        #      tmp = nums[index]
        #      if tmp > maximum:
        #          maximum = tmp
        #  second = -float('inf')
        #  for index in range(0, len(nums)):
        #      tmp = nums[index]
        #      if second < tmp and tmp < maximum:
        #          second = tmp
        #  if second == -float('inf'):
        #      return maximum
        #  third = -float('inf')
        #  for index in range(0, len(nums)):
        #      tmp = nums[index]
        #      if third < tmp and tmp < second:
        #          third = tmp
        #  if third == -float('inf'):
        #      return maximum
        #  return third
        """
        not using index would speed up
        """
        maximum = -float('inf')
        second = -float('inf')
        third = -float('inf')
        for num in nums:
            if num > second:
                if num > maximum:
                    third = second
                    second = maximum
                    maximum = num
                elif num < maximum:
                    third = second
                    second = num
            elif num < second:
                if num > third:
                    third = num
        if third == -float('inf'):
            return maximum
        return third


if __name__ == '__main__':
    test = Solution()
    #  print(test.thirdMax([3, 2, 1]))
    #  print(test.thirdMax([2, 1]))
    #  print(test.thirdMax([1]))
    print(test.thirdMax([2, 2, 3, 1]))
