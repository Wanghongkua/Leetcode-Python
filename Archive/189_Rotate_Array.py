from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #  if k % len(nums) == 0:
        #      return
        #  if not nums or len(nums) == 1:
        #      return

        #  k = k % len(nums)
        #  count = 0
        #  firstValue = 0
        #  while count < len(nums):
        #      buf = None
        #      previousBuf = nums[firstValue]
        #      index = k % len(nums) + firstValue

        #      while index != firstValue:
        #          buf = nums[index]
        #          nums[index] = previousBuf
        #          index = (index + k) % len(nums)
        #          previousBuf = buf
        #          count += 1
        #      nums[index] = previousBuf
        #      count += 1

        #      firstValue += 1
        """
        Calculate untouched number of element to be the new "k"
        """
        #  length = len(nums)
        #  k = k % length
        #  i = length-k-1
        #  while k:
        #      if i < 0:
        #          length, k = k, k-(length-length//k*k)
        #          i = length-k-1
        #          if length == k:
        #              break
        #      nums[i], nums[i+k] = nums[i+k], nums[i]
        #      i -= 1       # reverse(nums, k, len(nums) - 1)
        """
        Try to imporve by using reversed
        """
        def reverse(nums):
            start = 0
            end = len(nums) - 1
            tmp = None
            while start < end:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
                start += 1
                end -= 1
            return nums

        k = k % len(nums)
        nums = reverse(nums)
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])
        """
        Try to save space
        """

        print(nums)


if __name__ == '__main__':
    test = Solution()
    test.rotate([1, 2, 3, 4, 5, 6, 7], 4)
