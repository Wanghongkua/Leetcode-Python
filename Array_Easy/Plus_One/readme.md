### [Question](https://leetcode.com/problems/plus-one/)

Given a **non-empty** array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

**Example 1:**

```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```

**Example 2:**

```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

### Answers

Just need to test whether the current `digit` equals to `9`. Asign `0` when `true`, and `digit + 1` when `false`

```python
def plusOne(self, digits: List[int]) -> List[int]:
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
```
