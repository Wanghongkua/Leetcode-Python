from typing import List
from math import log2


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
        elements appear twice and others appear once.

        Find all the elements of [1, n] inclusive that do not appear in this
        array.

        Could you do it without extra space and in O(n) runtime? You may assume
        the returned list does not count as extra space.

        Example:
            Input:
            [4,3,2,7,8,2,3,1]

            Output:
            [5,6]
        """

        """
        simply use set
        """
        #  result = []
        #  testSet = set(nums)
        #  for num in range(1, len(nums)+1):
        #      if num not in testSet:
        #          result.append(num)

        #  return result
        """
        use bucket sort to save space
        """
        # result = []
        # testBucket = [None]*len(nums)

        # for item in nums:
        #     testBucket[item-1] = 1

        # for index in range(len(nums)):
        #     if not testBucket[index]:
        #         result.append(index+1)

        # return result
        """
        try use less space
        """
        print('0b' + '1' * int(log2(len(nums))))
        #  even = int('0b' + '1' * log2(len(nums)))
        #  odd = 0
        result = []

        return result


if __name__ == '__main__':
    test = Solution()
    print(test.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
