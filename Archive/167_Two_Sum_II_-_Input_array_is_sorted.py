from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #  numSet = {}
        #  for index in range(len(numbers)):
        #      ele = numbers[index]
        #      if ele not in numSet:
        #          numSet[ele] = [index + 1]
        #      else:
        #          numSet[ele].append(index + 1)
        #  for ele in numbers:
        #      if target - ele in numSet:
        #          if target - ele == ele:
        #              if len(numSet[ele]) > 1:
        #                  return numSet[ele][:2]
        #              continue
        #          return [numSet[ele][0], numSet[target-ele][0]]
        """
        try to improve
        """
        start = 0
        end = len(numbers) - 1
        while True:
            val = numbers[start] + numbers[end]
            if val > target:
                end -= 1
            elif val < target:
                start += 1
            else:
                return [start+1, end+1]


if __name__ == '__main__':
    test = Solution()
    print(test.twoSum([2, 7, 11, 15], 9))
