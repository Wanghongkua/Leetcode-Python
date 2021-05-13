from typing import List


class Solution:
    """
    Two Pointers
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        firstIndex = 0
        secondIndex = 1
        while secondIndex < len(nums):
            if nums[firstIndex] != nums[secondIndex]:
                if secondIndex - firstIndex > 1:
                    nums[firstIndex + 1] = nums[secondIndex]
                firstIndex += 1
                secondIndex += 1
            else:
                secondIndex += 1
        return firstIndex + 1


if __name__ == "__main__":
    test = Solution()
    print(test.removeDuplicates([1, 1, 2]))
    print(test.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
