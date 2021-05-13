# Automation

**`add2Readme.py`** can:

1. Add folder for each question, and generate `Python` file, `readme.md` file
   and `.gitignore` file with the new folder
2. Add links to `readme.md`

The using method is: `python add2Readme.py 53. Maximum Subarray`

**`update_ideas.py`** can search for comments of each python file and add that
to **basic ideas**, which requires the comment musk be a short introduction of
the answer.

## Leetcode Solutions for Python

This repository focuses on solving all Leetcode problems with Python. The layout
has two factors, which are tags and difficulty. Besides, there will be
explanation for each question.

### Array

#### Easy

| #   | Title                                     | Explanation     | Code            | Basic Ideas                                                                                             |
| --- | ----------------------------------------- | --------------- | --------------- | ------------------------------------------------------------------------------------------------------- |
| 1   | [Two Sum][1]                              | [Answer][1_a]   | [Python][1_c]   | 1. Hash Table<br>2. One-Pass Hash Table                                                                 |
| 26  | [Remove Duplicates from Sorted Array][26] | [Answer][26_a]  | [Python][26_c]  | 1. Two Pointers                                                                                         |
| 27  | [Remove Element][27]                      | [Answer][27_a]  | [Python][27_c]  | 1. Two Pointers                                                                                         |
| 35  | [Search Insert Position][35]              | [Answer][35_a]  | [Python][35_c]  | 1. Binary Search<br>2. Improvement on avoiding checking "middle" on mismatch<br>3. Less code but slower |
| 53  | [Maximum Subarray][53]                    | [Answer][53_a]  | [Python][53_c]  | 1. Dynamic Programming<br>2. Less code version of DP                                                    |
| 66  | [Plus One][66]                            | [Answer][66_a]  | [Python][66_c]  | 1. Test equal to `9`                                                                                    |
| 88  | [Merge Sorted Array][88]                  | [Answer][88_a]  | [Python][88_c]  | 1. Two Pointer<br>2. Optimisation for TP                                                                |
| 118 | [Pascals Triangle][118]                   | [Answer][118_a] | [Python][118_c] |                                                                                                         |

#### Hard

| #   | Title                            | Explanation   | Code          | BasicIdeas |
| --- | -------------------------------- | ------------- | ------------- | ---------- |
| 4   | [Median of Two Sorted Arrays][4] | [Answer][4_a] | [Python][4_c] |            |

[1]: https://leetcode.com/problems/two-sum/
[1_a]: Array/Easy/Two_Sum
[1_c]: Array/Easy/Two_Sum/Two_Sum.py
[4]: https://leetcode.com/problems/median-of-two-sorted-arrays/
[4_a]: Array/Hard/Median_of_Two_Sorted_Arrays/
[4_c]: Array/Hard/Median_of_Two_Sorted_Arrays/Median_of_Two_Sorted_Arrays.py
[26]: http://leetcode.com/problems/remove-duplicates-from-sorted-array/
[26_a]: Array/Easy/Remove_Duplicates_from_Sorted_Array
[26_c]: Array/Easy/Remove_Duplicates_from_Sorted_Array/Remove_Duplicates_from_Sorted_Array.py
[27]: https://leetcode.com/problems/remove-element/
[27_a]: Array/Easy/Remove_Element
[27_c]: Array/Easy/Remove_Element/Remove_Element.py
[35]: https://leetcode.com/problems/search-insert-position/
[35_a]: Array/Easy/Search_Insert_Position
[35_c]: Array/Easy/Search_Insert_Position/Search_Insert_Position.py
[53]: https://leetcode.com/problems/maximum-subarray/
[53_a]: Array/Easy/Maximum_Subarray/
[53_c]: Array/Easy/Maximum_Subarray/Maximum_Subarray.py
[66]: https://leetcode.com/problems/plus-one/
[66_a]: Array/Easy/Plus_One/
[66_c]: Array/Easy/Plus_One/Plus_One.py
[88]: https://leetcode.com/problems/merge-sorted-array/
[88_a]: Array/Easy/Merge_Sorted_Array/
[88_c]: Array/Easy/Merge_Sorted_Array/Merge_Sorted_Array.py
[118]: https://leetcode.com/problems/pascals-triangle/
[118_a]: Array/Easy/Pascals_Triangle/
[118_c]: Array/Easy/Pascals_Triangle/Pascals_Triangle.py
