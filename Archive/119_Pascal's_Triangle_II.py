from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        use same list to do dynamic computing
        """
        #  result = [None] * (rowIndex + 1)
        #  result[0] = 1
        #  for row in range(rowIndex + 1):
        #      index = row - 1
        #      while index >= 1:
        #          result[index] = result[index-1] + result[index]
        #          index -= 1
        #      result[row] = 1
        #  return result

        """
        improve speed
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        result = [None] * (rowIndex + 1)
        result[0] = 1
        result[1] = 1
        for row in range(2, rowIndex + 1):
            index = row - 1
            while index >= row // 2:
                result[index] = result[index-1] + result[index]
                index -= 1
            while index >= 1:
                result[index] = result[row - index]
                index -= 1
            result[row] = 1
        return result


if __name__ == '__main__':
    test = Solution()
    print(test.getRow(4))
