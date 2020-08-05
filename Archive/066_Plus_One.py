from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        plus = 1
        while plus:
            val = digits[index] + 1
            if val >= 10:
                digits[index] = val % 10
                index -= 1
                if index < 0:
                    return [1] + digits
                plus = 1
            else:
                digits[index] = val
                plus = 0
        return digits


if __name__ == "__main__":
    test = Solution()
    print(test.plusOne([9]))
    print(test.plusOne([1, 2, 3]))
    print(test.plusOne([4, 3, 2, 1]))
