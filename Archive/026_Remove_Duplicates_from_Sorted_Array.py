from typing import List


class Solution:
    #  def removeDuplicates(self, nums: List[int]) -> int:
    #      if len(nums) < 2:
    #          return len(nums)

    #      previous = 0
    #      current = 1
    #      while True:
    #          if nums[current] != nums[previous]:
    #              if current - 1 == previous:
    #                  current += 1
    #                  previous += 1
    #              else:
    #                  nums[previous:current] = [nums[previous], nums[current]]
    #                  previous += 1
    #                  current = previous + 1
    #          else:
    #              current += 1

    #          if current >= len(nums):
    #              break

    #      if current - previous > 1:
    #          nums[previous:] = [nums[previous]]

    #      return len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        previous = 0
        current = 1
        while current < len(nums):
            if nums[current] != nums[previous]:
                if current - 1 == previous:
                    current += 1
                    previous += 1
                else:
                    nums[previous+1] = nums[current]
                    previous += 1
                    current += 1
            else:
                current += 1

        if nums[previous] == nums[-1]:
            return previous + 1
        else:
            return previous + 2


if __name__ == "__main__":
    test = Solution()
    print(test.removeDuplicates([1, 1, 2]))
    print(test.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
