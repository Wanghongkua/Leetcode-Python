from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        The easiest way
        """
        #  numDic = {}
        #  for item in nums:
        #      if item in numDic:
        #          numDic[item] += 1
        #      else:
        #          numDic[item] = 1
        #  for val, count in numDic.items():
        #      if count > len(nums) / 2:
        #          return val

        """
        Try make it faster by using hash table
        """
        #  numDic = {}
        #  for item in nums:
        #      if item in numDic:
        #          numDic[item] += 1
        #      else:
        #          numDic[item] = 1
        #  for val, count in numDic.items():
        #      if count > len(nums) / 2:
        #          return val
        """
        Boyer Moore
        """
        count = 0
        candidate = None
        for ele in nums:
            if count == 0:
                candidate = ele
            count += (1 if ele == candidate else -1)
        return candidate


if __name__ == '__main__':
    test = Solution()
    print(test.majorityElement([3, 2, 3]))
