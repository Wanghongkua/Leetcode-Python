### [Question](https://leetcode.com/problems/two-sum/)

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **_exactly_** one solution, and you may not use the same element twice.

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

### Answers

####  Hash Table

Using **hash table** to build an inverted index, where keys are the items of `nums`, and values are arrays formed by the
indexes of keys. In this way we can avoid the second index being the same with the first one.

#### One-Pass Hash Table

While building the hash table, we can always look back to see if there is a match. In this way, we only need to iterate
`nums` for once. Because there is exactly one solution, we only need to store the index of each item in `nums` once.
