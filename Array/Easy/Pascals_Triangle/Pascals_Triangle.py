from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Dynamic Programming
        """
        #  result = []
        #  for row in range(numRows):
        #      rowResult = [None] * (row + 1)

        #      # add "1" to beginning and end
        #      rowResult[0], rowResult[-1] = 1, 1

        #      # add rest
        #      for index in range(1, row):
        #          rowResult[index] = result[row - 1][index - 1] + result[row - 1][index]

        #      result.append(rowResult)
        #  return result
        """
        DP that only calculate first half of rowResult
        """
        #  result = []
        #  for row in range(numRows):
        #      rowResult = [None] * (row + 1)

        #      # add "1" to beginning and end
        #      rowResult[0], rowResult[-1] = 1, 1

        #      # add rest
        #      if (row + 1) % 2 == 0:
        #          middle = (row + 1) // 2
        #      else:
        #          middle = (row + 1) // 2 + 1

        #      # add first half of rowResult
        #      for index in range(1, middle):
        #          rowResult[index] = result[row - 1][index - 1] + result[row - 1][index]

        #      # add second half of rowResult
        #      for index in range(middle, row):
        #          rowResult[index] = rowResult[row - index]

        #      result.append(rowResult)
        #  return result
        """
        DP faster by not using `for...range():`
        """
        result = []
        for row in range(numRows):
            rowResult = [None] * (row + 1)

            # add "1" to beginning and end
            rowResult[0], rowResult[-1] = 1, 1

            # add rest
            if (row + 1) % 2 == 0:
                middle = (row + 1) // 2
            else:
                middle = (row + 1) // 2 + 1

            # add first half of rowResult
            index = 1
            while index < middle:
                rowResult[index] = result[row - 1][index -
                                                   1] + result[row - 1][index]
                index += 1

            # add second half of rowResult
            while index < row:
                rowResult[index] = rowResult[row - index]
                index += 1

            result.append(rowResult)
        return result


if __name__ == "__main__":
    test = Solution()
    print(test.generate(5))
