### [Question](https://leetcode.com/problems/remove-element/)

Given an array nums and a value _val_, remove all instances of that value [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) and return the new length.

Do not allocate extra space for another array, you must do this by **modifying the input array** in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

**Example 1:**

```
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
```

**Example 2:**

```
Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
```

**Clarification:**

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by **reference**, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

### Answers

#### Two Pointers

The reasons why two pointers method is appropriate are:

1. There is 2 positions involved
2. The information traversed is not needed, so they don't need to look back
   > **i.e.**, Only the items that are equal to `val` is needed.

There are 2 steps involved:

1. find the index for replacement of `val` from the end of list `nums`.
2. replace

```python
def removeElement(self, nums: List[int], val: int) -> int:
    replaceIndex = len(nums) - 1
    index = 0

    while index <= replaceIndex:
        if nums[replaceIndex] == val:
            replaceIndex -= 1
            continue
        if nums[index] == val:
            nums[index] = nums[replaceIndex]
            replaceIndex -= 1
        index += 1
    return index
```

**Alternatives**

1. replace each item from the back of list `nums`, until a non `val` value is found
2. increase `index`

```python
def removeElement(self, nums: List[int], val: int) -> int:
    replaceIndex = len(nums) - 1
    index = 0

    while index <= replaceIndex:
        if nums[index] == val:
            nums[index] = nums[replaceIndex]
            replaceIndex -= 1
        else:
            index += 1
    return index
```

**Comparison**

For the items which are equal to `val` at the **back** of list `nums`, the **alternative** involves a lot of meaningless
copy of items that are equal to `val`, and the actions are:

1. compare `replaceIndex` with `index`
2. compare `nums[index]` with `val`
3. list read: `nums[replaceIndex]`
4. list write: `nums[index]`
5. decrease `replaceIndex`

While my the first method only need these actions:

1. compare `replaceIndex` with `index`
2. compare `nums[replaceIndex]` with `val`
3. decrease `replaceIndex`
