from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) \
            -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #  start = 0
        #  end = m - 1
        #  for index in range(n):
        #      val = nums2[index]
        #      position = None
        #      while end - start > 1:
        #          middle = (start + end) // 2
        #          if nums1[middle] >= val:
        #              end = middle
        #          else:
        #              start = middle + 1
        #      if nums1[start] >= val:
        #          position = start
        #      elif nums1[end] < val:
        #          position = end + 1
        #      else:
        #          position = end

        #      nums1[position + 1:m + index + 1] = nums1[position:m + index]

        #      nums1[position] = val
        #      start = position
        #      end = m + index
        positions = [None] * n
        start = 0
        end = m - 1
        for index in range(n):
            val = nums2[index]
            position = None
            while end - start > 1:
                middle = (start + end) // 2
                if nums1[middle] >= val:
                    end = middle
                else:
                    start = middle
            if nums1[start] >= val:
                position = start
            elif nums1[end] < val:
                position = end + 1
            else:
                position = end
            positions[index] = position
            start = position
            end = m - 1
        index = n - 1
        end = m
        while n >= 0:
            try:
                nums1[positions[index]:end + index + 1] = nums1[positions[index - 1]]
            except Exception as e:
                raise e

            index -= 1


if __name__ == '__main__':
    test = Solution()
    test.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
    test.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
