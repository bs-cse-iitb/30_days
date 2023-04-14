class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {} # value: index
        for i,ele in enumerate(nums):
            diff = target - ele
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[ele] = i