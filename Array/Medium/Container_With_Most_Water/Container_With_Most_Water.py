from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_mask = [0] * len(height)
        right_mask = [0] * len(height)

        largest = -1
        for index, value in enumerate(height):
            if value > largest:
                left_mask[index] = 1
                largest = value
        largest = -1
        index = len(height) - 1
        while index >= 0:
            if height[index] > largest:
                right_mask[index] = 1
                largest = height[index]
            index -= 1
        print(left_mask)
        print(right_mask)
        return 0


if __name__ == "__main__":
    inputs = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
    ]
    test = Solution()
    for i, result in inputs:
        test_result = test.maxArea(i)
        if test_result != result:
            print(i, "\n", "Expected:", result,
                  "\n", "Output:", test_result)
