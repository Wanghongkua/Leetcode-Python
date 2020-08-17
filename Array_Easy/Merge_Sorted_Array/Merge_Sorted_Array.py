from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Two Pointer
        """
        #  index1 = m - 1
        #  index2 = n - 1
        #  index = m + n - 1
        #  while True:
        #      if index1 < 0:
        #          nums1[:index2 + 1] = nums2[:index2 + 1]
        #          break
        #      if index2 < 0:
        #          break
        #      if nums2[index2] >= nums1[index1]:
        #          nums1[index] = nums2[index2]
        #          index -= 1
        #          index2 -= 1
        #      else:
        #          nums1[index] = nums1[index1]
        #          index -= 1
        #          index1 -= 1
        """
        Optimisation for TP
        """
        index1 = m - 1
        index2 = n - 1
        index = m + n - 1
        while index1 > -1 and index2 > -1:
            if nums2[index2] >= nums1[index1]:
                nums1[index] = nums2[index2]
                index2 -= 1
            else:
                nums1[index] = nums1[index1]
                index1 -= 1
            index -= 1
        if index2 > -1:
            nums1[:index2 + 1] = nums2[:index2 + 1]


if __name__ == "__main__":
    test = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    test.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    test.merge(nums1, m, nums2, n)
    print(nums1)
