from typing import List


class Solution:
    #  def removeElement(self, nums: List[int], val: int) -> int:
    #     # Slow version
    #     start = 0
    #     end = len(nums)
    #     while end > start:
    #         if nums[start] != val:
    #             start += 1
    #             continue
    #         nums[start] = nums[end - 1]
    #         end -= 1
    #      return start

    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        start = 0
        end = len(nums) - 1
        while True:
            try:
                while nums[start] != val:
                    start += 1

                while nums[end] == val:
                    end -= 1
            except IndexError:
                break

            if start >= end:
                break
            nums[start] = nums[end]
            nums[end] = val

        return start


if __name__ == "__main__":
    test = Solution()
    print(test.removeElement([3, 2, 2, 3], 3))
    print(test.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
