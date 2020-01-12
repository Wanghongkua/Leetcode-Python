from typing import List


class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     start = 0
    #     end = len(nums) - 1
    #     while True:
    #         if end - start <= 1:
    #             if nums[start] >= target:
    #                 return start
    #             elif nums[end] < target:
    #                 return end + 1
    #             else:
    #                 return end
    #         middle = (start + end) // 2
    #         if nums[middle] > target:
    #             end = middle
    #         else:
    #             start = middle

    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     start = 0
    #     end = len(nums) - 1
    #     while start <= end:
    #         middle = (start + end) // 2
    #         if nums[middle] >= target:
    #             end = middle - 1
    #         else:
    #             start = middle + 1
    #     return start

    #  def searchInsert(self, nums: List[int], target: int) -> int:
    #      start = 0
    #      end = len(nums) - 1
    #      while end > start:
    #          middle = (start + end) // 2
    #          if nums[middle] >= target:
    #              end = start
    #          else:
    #              start = middle + 1

    #      if nums[start] >= target:
    #          return start
    #      else:
    #          return start + 1

    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while end - start > 1:
            middle = (start + end) // 2
            if nums[middle] >= target:
                end = middle
            else:
                start = middle

        if nums[start] >= target:
            return start
        elif nums[end] < target:
            return end + 1
        else:
            return end


if __name__ == "__main__":
    test = Solution()
    print(test.searchInsert([1, 3, 5, 6], 5))
    print(test.searchInsert([1, 3, 5, 6], 2))
    print(test.searchInsert([1, 3, 5, 6], 7))
    print(test.searchInsert([1, 3, 5, 6], 0))
