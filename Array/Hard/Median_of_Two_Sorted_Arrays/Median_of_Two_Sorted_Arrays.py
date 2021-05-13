from typing import List


class Solution:
    def findSingleArrayMedian(self, nums: List[int]) -> float:
        """Find the median number of a single array"""
        length = len(nums)
        median = None
        if length % 2 != 0:
            median = float(nums[length // 2])
        else:
            median = (nums[length // 2] + nums[length // 2 - 1]) / 2
        return median

    def findMedianPosition(self, length1: int, length2: int) -> int:
        """Find the required start index of median"""
        length_sum = length1 + length2
        if length_sum % 2 != 0:
            return length_sum // 2
        else:
            return length_sum // 2 - 1

    def calculateMedian(self, nums1: List[int], nums2: List[int],
                        median_index: int, median_position: int) -> float:
        """calculate the actual median value"""
        #  single median
        if (len(nums1) + len(nums2)) % 2 != 0:
            return float(nums1[median_index])

        #  double median
        nums1_median = None
        if median_index + 1 < len(nums1):
            nums1_median = median_index + 1

        nums2_median = None
        if median_position - median_index < len(nums2):
            nums2_median = median_position - median_index

        if nums1_median is None:
            return (nums1[median_index] + nums2[nums2_median]) / 2
        elif nums2_median is None:
            return (nums1[median_index] + nums1[nums1_median]) / 2
        elif nums1[nums1_median] < nums2[nums2_median]:
            return (nums1[median_index] + nums1[nums1_median]) / 2
        else:
            return (nums1[median_index] + nums2[nums2_median]) / 2

    def testMedian(self, median: int, nums: List[int], start: int, end: int)\
            -> int:
        if median < nums[start]:
            return 1
        if median > nums[end]:
            return 2
        return 0

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) \
            -> float:
        # One of the array is empty
        if not nums1:
            return self.findSingleArrayMedian(nums2)
        elif not nums2:
            return self.findSingleArrayMedian(nums1)

        # Use shorter array to speed up
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        nums1_start = 0
        nums1_end = len(nums1) - 1
        nums2_start = 0
        nums2_end = len(nums2) - 1

        # The concatenation of 2 arrays is sorted
        if nums1[nums1_end] <= nums2[nums2_start]:
            return self.findSingleArrayMedian(nums1 + nums2)
        elif nums1[nums1_start] >= nums2[nums2_end]:
            return self.findSingleArrayMedian(nums2 + nums1)

        median_position = self.findMedianPosition(len(nums1), len(nums2))
        median_index = 0
        nums1_middle = 0
        in_nums2 = True
        test_result = -1

        # The median exists in the middle of one array,
        while nums1_start - nums1_end <= 0 and nums2_start - nums2_end <= 0:
            nums1_middle = (nums1_start + nums1_end) // 2
            nums2_middle = median_position - (nums1_middle + 1)

            # len(nums1) == len(nums2) and nums1[-1] is nums1_middle
            # Because nums1[-1] > nums2[0], nums2[0] is the median
            if nums2_middle < 0:
                test_result = 0
                median_index = 0
                break

            test_result = self.testMedian(nums1[nums1_middle], nums2,
                                          nums2_middle, nums2_middle + 1)
            if not test_result:
                median_index = nums1_middle
                in_nums2 = False
                break
            elif test_result == 1:
                nums1_start = nums1_middle + 1
                nums2_end = nums2_middle
            else:
                nums1_end = nums1_middle - 1
                nums2_start = nums2_middle + 1

        #  Median in nums2
        if in_nums2:
            #  Median is nums2[0]
            if test_result == 0:
                pass
            # nums1_middle position included
            elif test_result == 1:
                median_index = median_position - 1 - nums1_middle
            # nums1_middle position not included
            else:
                median_index = median_position - 1 - (nums1_middle - 1)
            #  median_index = median_position - 1 - nums1_middle
            return self.calculateMedian(nums2, nums1,
                                        median_index, median_position)
        #  Median in nums1
        return self.calculateMedian(nums1, nums2,
                                    median_index, median_position)


if __name__ == "__main__":
    inputs = [
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1, 3], [2], 2.0),
        ([1, 3], [2, 7], 2.5),
        ([1, 3, 4], [2], 2.5),
    ]
    test = Solution()
    for i, j, result in inputs:
        test_result = test.findMedianSortedArrays(i, j)
        if test_result != result:
            print(i, j, "\n", "Expected:", result,
                  "\n", "Output:", test_result)
