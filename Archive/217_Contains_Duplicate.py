from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #  if len(nums) != len(set(nums)):
        #      return True
        #  return False
        """
        Improve by using less checking
        """
        #  numsDic = {}
        #  for item in nums:
        #      if item not in numsDic:
        #          numsDic[item] = 1
        #      else:
        #          return True
        #  return False
        """
        change to set
        """
        numsSet = set()
        for item in nums:
            if item not in numsSet:
                numsSet.add(item)
            else:
                return True
        return False


if __name__ == '__main__':
    test = Solution()
    print(test.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
