from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Most simple one
        """
        #  numsSet = set(nums)
        #  for count in range(len(nums)+1):
        #      if count not in numsSet:
        #          return count
        """
        Try to improve space by using in-place switch
        """
        #  index = 0
        #  while index < len(nums):
        #      if nums[index] == len(nums):
        #          index += 1
        #          continue
        #      if nums[index] != index:
        #          tmp = nums[nums[index]]
        #          nums[nums[index]] = nums[index]
        #          nums[index] = tmp
        #          continue
        #      index += 1
        #  for index in range(len(nums)):
        #      if nums[index] != index:
        #          return index
        #  return len(nums)
        """
        Try improve speed by Gauss' Formula
        """
        #  total = len(nums)*(len(nums)+1) // 2
        #  for item in nums:
        #      total -= item
        #  return total
        """
        Using Xor to eliminate all the occurance
        """
        missing = 0
        for index in range(1, len(nums)+1):
            missing ^= index
        for item in nums:
            missing ^= item
        return missing


if __name__ == '__main__':
    test = Solution()
    print(test.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
