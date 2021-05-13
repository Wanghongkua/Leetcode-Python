from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Binary Search
        """
        #  index = len(nums) // 2
        #  start = 0
        #  end = len(nums) - 1
        #  while start != index:
        #      if nums[index] == target:
        #          return index
        #      if nums[index] < target:
        #          start = index
        #          index = (index + end) // 2
        #      else:
        #          end = index
        #          index = (index + start) // 2

        #  if target <= nums[index]:
        #      return start
        #  if target > nums[end]:
        #      return end + 1
        #  return end
        """
        Improvement on avoiding checking "middle" on mismatch
        """
        #  start = 0
        #  end = len(nums) - 1
        #  while start < end:
        #      middle = (start + end) // 2
        #      if nums[middle] < target:
        #          start = middle + 1
        #      elif nums[middle] > target:
        #          end = middle
        #      else:
        #          start = middle
        #          break
        #  if nums[start] >= target:
        #      return start
        #  else:
        #      return start + 1
        """
        Less code but slower
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            middle = (start + end) // 2
            if nums[middle] < target:
                start = middle + 1
            else:
                end = middle
        if nums[start] >= target:
            return start
        else:
            return start + 1


if __name__ == "__main__":
    test = Solution()
    print(test.searchInsert([1, 3, 5, 6], 5))
    print(test.searchInsert([1, 3, 5, 6], 2))
    print(test.searchInsert([1, 3, 5, 6], 7))
    print(test.searchInsert([1, 3, 5, 6], 0))
    print(test.searchInsert([1, 3], 1))
