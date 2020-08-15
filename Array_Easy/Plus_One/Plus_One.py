from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Test equal to `9`
        """
        index = len(digits) - 1
        while index >= 0:
            val = digits[index]
            if val < 9:
                digits[index] = val + 1
                return digits
            digits[index] = 0
            index -= 1
        digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    test = Solution()
    digits = [9, 9, 9, 9]
    digits = test.plusOne(digits)
    print(digits)

    digits = [9]
    digits = test.plusOne(digits)
    print(digits)

    digits = [1, 9]
    digits = test.plusOne(digits)
    print(digits)

    digits = [1, 2, 3]
    digits = test.plusOne(digits)
    print(digits)
