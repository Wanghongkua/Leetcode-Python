class Solution(object):
    '''
    Given an array of integers, find two numbers such that they add up to a
    specific target number.

    The function twoSum should return indices of the two numbers such that they
    add up to the target,
    where index1 must be less than index2.
    Please note that your returned answers (both index1 and index2) are not
    zero-based.

    You may assume that each input would have exactly one solution.

    Input: numbers={2, 7, 11, 15}, target=9
    Output: index1=1, index2=2


    '''

#    def twoSum(self, nums, target):
#        """ hash 1
#
#        nums:    List[int]
#        target:  int
#        returns: List[int]
#
#        """
#        result = None
#        numsDict = {}
#        for i in range(len(nums)):
#            if nums[i] not in numsDict:
#                numsDict[nums[i]] = 1
#            else:
#                numsDict[nums[i]] += 1
#
#        for i in range(len(nums)):
#            numsDict[nums[i]] -= 1
#            if target - nums[i] in numsDict \
#                    and numsDict[target-nums[i]] > 0:
#                result = [i, None]
#            else:
#                numsDict[nums[i]] += 1
#
#        for i in range(result[0]+1, len(nums)):
#            if nums[i] == target - nums[result[0]]:
#                result[1] = i
#                break
#
#        return result

    def twoSum(self, nums, target):
        # hash2
        hash_nums = {}
        for index, val in enumerate(nums):
            try:
                hash_nums[target-val]
                return [index, hash_nums[target-val]]
            except KeyError:
                hash_nums[val] = index


test = Solution()
print(test.twoSum([3, 3], 6))
