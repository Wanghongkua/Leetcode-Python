from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #  result = [[None]*(row + 1) for row in range(numRows)]
        #  for row in range(numRows):
        #      result[row][0] = 1
        #      result[row][-1] = 1
        #      try:
        #          for index in range(1, row):
        #              result[row][index] = \
        #                  result[row - 1][index - 1] + result[row - 1][index]
        #      except Exception:
        #          pass
        #  return result
        """
        COMP9021 Version
        """
        #  result = [[1] * (row + 1) for row in range(numRows)]
        #  for row in range(2, numRows):
        #      for index in range(1, row // 2 + 1):
        #          result[row][index] = \
        #              result[row - 1][index - 1] + result[row - 1][index]
        #      for index in range(1, (row + 1) // 2):
        #          result[row][row - index] = result[row][index]
        #  return result
        """
        Compbined version
        """
        #  result = [[1]*(row + 1) for row in range(numRows)]
        #  for row in range(2, numRows):
        #      for index in range(1, row):
        #          result[row][index] = \
        #              result[row - 1][index - 1] + result[row - 1][index]
        #  return result
        """
        Improved Compbined version
        """
        result = [[None] * (row + 1) for row in range(numRows)]
        for row in range(numRows):
            result[row][0] = 1
            result[row][-1] = 1
            for index in range(1, row // 2 + 1):
                result[row][index] = \
                    result[row - 1][index - 1] + result[row - 1][index]
            for index in range(1, (row + 1) // 2):
                result[row][row - index] = result[row][index]
        return result


if __name__ == '__main__':
    test = Solution()
    print(test.generate(5))
