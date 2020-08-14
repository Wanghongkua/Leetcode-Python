### [Question](http://leetcode.com/problems/maximum-subarray/)

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Follow up:**

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

### Answers

#### Train of Thought

**Idea**

For finding a contiguous sub-array with maximum sum, which must has an **ending point** with zero to arbitrary number of
preceding elements.

**Thinking Steps**

1. We can compare the sub-arrays that end with the same index in `nums`, and find the largest one.
    1. If we have the sub-array with largest sum of previous index, the largest sum of current index can be found either
       by extend the previous sub-array to current index, or just current index if that sum is negative.
    2. found the largest sum of the first index.
2. Compare the selected sub-arrays from previous step of each index, and find the one that has the maximum sum.

#### Summary

The reasons why Dynamic Programming is suitable here are:

1. The problem can be break down into sub-problems, which can be solved recursively
   > i.e. **f(x)** = a**f(x-1)** + b**x**
2. The first sub-problem can be solved
   > i.e. **f(1)**, or **f(0)** in computer science, can be culculated

#### Dynamic Programming

Now the task is changed to find the 

```python
def maxSubArray(self, nums: List[int]) -> int:
    maximum = -float("inf")
    localMaximum = -float("inf")
    for index in range(len(nums)):
        if localMaximum + nums[index] < nums[index]:
            localMaximum = nums[index]
        else:
            localMaximum += nums[index]
        if localMaximum > maximum:
            maximum = localMaximum
    return maximum
```

Less code version

```python
def maxSubArray(self, nums: List[int]) -> int:
    localMaximum = maximum = nums[0]
    for index in range(1, len(nums)):
        localMaximum = max(localMaximum + nums[index], nums[index])
        maximum = max(localMaximum, maximum)
    return maximum
```
