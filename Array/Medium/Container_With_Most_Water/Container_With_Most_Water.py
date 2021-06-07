from typing import List


class Solution:
    def calculateSize(self, height: List[int], left: int, right: int) -> int:
        """Calculate current size based on the selected barrier"""
        high = min(height[left], height[right])
        return high * (right - left)

    def maxArea(self, height: List[int]) -> int:
        """
        Get all barriers first
        """
        #  left_candidates = []
        #  right_candidates = []

        #  # left candidates
        #  largest = -1
        #  for index, value in enumerate(height):
        #      if value > largest:
        #          left_candidates.append([value, index])
        #          largest = value

        #  # right candidates
        #  largest = -1
        #  index = len(height) - 1
        #  while index >= 0:
        #      if height[index] > largest:
        #          right_candidates.append([height[index], index])
        #          largest = height[index]
        #      index -= 1

        #  largest = -1
        #  left_index = 0
        #  right_index = 0
        #  while left_index < len(left_candidates) and \
        #          right_index < len(right_candidates):
        #      left_value = left_candidates[left_index][0]
        #      right_value = right_candidates[right_index][0]
        #      local_max = min(left_value, right_value) * \
        #          (right_candidates[right_index][1] -
        #           left_candidates[left_index][1])
        #      if local_max > largest:
        #          largest = local_max
        #      if left_value <= right_value:
        #          left_index += 1
        #      else:
        #          right_index += 1
        #  return largest

        """
        Two Pointers
        """
        largest = -1
        left_index = 0
        right_index = len(height) - 1
        left_max = -1
        right_max = -1
        while left_index < right_index:
            if height[left_index] >= left_max:
                left_max = height[left_index]
            else:
                left_index += 1
                continue
            if height[right_index] >= right_max:
                right_max = height[right_index]
            else:
                right_index -= 1
                continue
            local_max = self.calculateSize(height, left_index, right_index)
            if local_max > largest:
                largest = local_max
            if height[left_index] <= height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        return largest


if __name__ == "__main__":
    inputs = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([1, 3, 2, 5, 25, 24, 5], 24),
        ([2, 3, 10, 5, 7, 8, 9], 36),
    ]
    test = Solution()
    for i, result in inputs:
        test_result = test.maxArea(i)
        if test_result != result:
            print(i, "\n", "Expected:", result,
                  "\n", "Output:", test_result)
