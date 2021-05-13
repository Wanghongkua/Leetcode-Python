### [Question](http://leetcode.com/problems/merge-sorted-array/)

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

**Note:**

- The number of elements initialized in nums1 and nums2 are m and n respectively.
- You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

**Example:**

```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

### Answers

#### Train of Thought

The elements within those 2 lists must be checked for at least 1 time in worst case scenario. This problem can be viewed
as a variation of [Search Insertion Position](../Search_Insert_Position/), as the only difference is the number of
elements needed to be inserted.

When inserting, if we start from the beginning, we may need to move the whole list of `nums1` for every insertion.
However, if we look closely at `nums1`, there are plenty of space at the end. If we put the largest element at the end
of `nums1` each time, no shifting is needed. Therefore, starting from the end of `nums1` becomes a natural choice.

#### Summary

The answer is a variation of **two pointers**. The first pointer is the insertion position, the other "_pointer_" is the
item needed to be inserted. The second pointer can be viewed as a variable of the next largest item within 2 lists.

The reason why two pointer is suitable is because:

1. There is 2 pointers involved
2. Those 2 lists are sorted, so the items traversed are not needed.

```python
def merge(self, nums1: List[int], m: int, nums2: List[int],
    index1 = m - 1
    index2 = n - 1
    index = m + n - 1
    while True:
        if index1 < 0:
            nums1[:index2 + 1] = nums2[:index2 + 1]
            break
        if index2 < 0:
            break
        if nums2[index2] >= nums1[index1]:
            nums1[index] = nums2[index2]
            index -= 1
            index2 -= 1
        else:
            nums1[index] = nums1[index1]
            index -= 1
            index1 -= 1
```

#### Optimisation

1. Avoid checking `index1` and `index2` within `while` loop.
2. Move decrementing of `index` outside of `if` clause.

```python
def merge(self, nums1: List[int], m: int, nums2: List[int],
    index1 = m - 1
    index2 = n - 1
    index = m + n - 1
    while index1 > -1 and index2 > -1:
        if nums2[index2] >= nums1[index1]:
            nums1[index] = nums2[index2]
            index2 -= 1
        else:
            nums1[index] = nums1[index1]
            index1 -= 1
        index -= 1
    if index2 > -1:
        nums1[:index2 + 1] = nums2[:index2 + 1]
```
