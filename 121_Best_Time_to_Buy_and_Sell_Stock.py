from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        most obvious way
        """
        #  result = 0
        #  for i in range(len(prices) - 1):
        #      localMax = 0
        #      for j in range(i, len(prices)):
        #          tmp = prices[j] - prices[i]
        #          if tmp > localMax:
        #              localMax = tmp
        #      if localMax > result:
        #          result = localMax
        #  return result
        """
        try to improve by call less in list
        """
        #  result = 0
        #  for i in range(len(prices) - 1):
        #      localMax = prices[i]
        #      for j in range(i, len(prices)):
        #          tmp = prices[j]
        #          if tmp > localMax:
        #              localMax = tmp
        #      if localMax - prices[i] > result:
        #          result = localMax - prices[i]
        #  return result
        """
        try to improve by skip continue descending element
        """
        if not prices:
            return 0
        smallest = prices[0]
        biggest = prices[0]
        maximum = 0
        for element in prices[1:]:
            if element > biggest:
                biggest = element
            if element < smallest:
                localMax = biggest - smallest
                if localMax > maximum:
                    maximum = localMax
                smallest = element
                biggest = element

        localMax = biggest - smallest
        if localMax > maximum:
            maximum = localMax

        return maximum


if __name__ == '__main__':
    test = Solution()
    print(test.maxProfit([7, 1, 5, 3, 6, 4]))
