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

        """
        Build a list a insertion positions of nums2 in nums1, then calculate
        the index of each element in nums1 and nums2
        """
        #  positions = [None] * n
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
        #              start = middle
        #      if nums1[start] >= val:
        #          position = start
        #      elif nums1[end] < val:
        #          position = end + 1
        #      else:
        #          position = end
        #      positions[index] = position
        #      start = position
        #      end = m - 1

        #  index = n - 1
        #  end = m
        #  while index >= 0:
        #      start = positions[index]

        #      nums1[start + index + 1:end + index + 1] = \
        #          nums1[start:end]
        #      nums1[positions[index]+index] = nums2[index]

        #      index -= 1
        #      end = start

        #  positions = [None] * n

        #  if m == 0:
        #      nums1[:] = nums2[:]
        #      return

        """
        calculate the insertion position for each element in nums2, then
        calculate the index of each element
        """

        #  start = 0
        #  end = m - 1
        #  ending = m
        #  index = n - 1
        #  while index >= 0:
        #      val = nums2[index]
        #      insert = None
        #      while end - start > 1:
        #          middle = (start + end) // 2
        #          if nums1[middle] >= val:
        #              end = middle
        #          else:
        #              start = middle
        #      if nums1[start] >= val:
        #          insert = start
        #      elif nums1[end] < val:
        #          insert = end + 1
        #      else:
        #          insert = end

        #      nums1[insert + index + 1:ending + index + 1] = \
        #          nums1[insert:ending]
        #      nums1[insert+index] = val
        #      ending = insert

        #      end = insert - 1
        #      start = 0
        #      index -= 1

        """
        insert element one by one
        """
        i = m - 1
        j = n - 1
        index = m + n - 1

        while True:
            if i < 0:
                nums1[0:index + 1] = nums2[0:j + 1]
                break
            if j < 0:
                break
            if nums1[i] < nums2[j]:
                nums1[index] = nums2[j]
                j -= 1
            else:
                nums1[index] = nums1[i]
                i -= 1
            index -= 1

        print(nums1)


if __name__ == '__main__':
    test = Solution()
    #  test.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
    #  test.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    #  test.merge([0, 0, 0, 0, 0], 0, [1, 2, 3, 4, 5], 5)
    test.merge([0, 0, 3, 0, 0, 0, 0, 0, 0], 3, [-1, 1, 1, 1, 2, 3], 6)
    test.merge([0], 0, [1], 1)
