### [Question](http://leetcode.com/problems/search-insert-position/)

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

**Example 1:**

```
Input: [1,3,5,6], 5
Output: 2
```

**Example 2:**

```
Input: [1,3,5,6], 2
Output: 1
```

**Example 3:**

```
Input: [1,3,5,6], 7
Output: 4
```

**Example 4:**

```
Input: [1,3,5,6], 0
Output: 0
```

### Answer

This is a binary search question, the key is to find the insertion point if `target` does not exist in `nums`. When the
final gap (length of 2) is found, use `target` to find the insertion point.

```python
def searchInsert(self, nums: List[int], target: int) -> int:
    index = len(nums) // 2
    start = 0
    end = len(nums) - 1
    while start != index:
        if nums[index] == target:
            return index
        if nums[index] < target:
            start = index
            index = (index + end) // 2
        else:
            end = index
            index = (index + start) // 2

    if target <= nums[index]:
        return start
    if target > nums[end]:
        return end + 1
    return end
```

#### Optimisation

1. Because `index` is not needed outside of `while` loop (`start` has the same vale of `index`), we can define `index`
inside `while` loop
2. After checking `nums[index]` in `while` loop, `index` should not be included in the new index gap. In other words,
   `start` should be assigned with `index + 1`, when `nums[index] < target`.

```python
def searchInsert(self, nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    while start < end:
        middle = (start + end) // 2
        if nums[middle] < target:
            start = middle + 1
        elif nums[middle] > target:
            end = middle
        else:
            start = middle
            break
    if nums[start] >= target:
        return start
    else:
        return start + 1
```

This can be further optimized to the following by deleting checking equal for `nums[middle]` with `target`. This will
slow the code, but looks cleaner.

```python
def searchInsert(self, nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    while start < end:
        middle = (start + end) // 2
        if nums[middle] < target:
            start = middle + 1
        else:
            end = middle
    if nums[start] >= target:
        return start
    else:
        return start + 1
```
