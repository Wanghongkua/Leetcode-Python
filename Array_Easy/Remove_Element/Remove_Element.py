from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Two Pointers
        """
        replaceIndex = len(nums) - 1
        index = 0

        while index <= replaceIndex:
            if nums[replaceIndex] == val:
                replaceIndex -= 1
                continue
            if nums[index] == val:
                nums[index] = nums[replaceIndex]
                replaceIndex -= 1
            index += 1
        return index


if __name__ == "__main__":
    test = Solution()
    print(test.removeElement([3, 2, 2, 3], 3))
    print(test.removeElement([1], 1))
    print(test.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
