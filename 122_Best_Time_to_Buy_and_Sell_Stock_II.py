from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        previous = prices[0]
        localMin = prices[0]
        maximum = 0
        status = 0
        for element in prices[1:]:
            if element < previous:
                if status == 2:
                    maximum += previous - localMin
                status = 1

            if element > previous:
                if status == 1:
                    localMin = previous
                status = 2

            previous = element

        if status == 2:
            maximum += previous - localMin

        return maximum


if __name__ == '__main__':
    test = Solution()
    #  print(test.maxProfit([7, 1, 5, 3, 6, 4]))
    print(test.maxProfit([7, 6, 4, 3, 1]))
