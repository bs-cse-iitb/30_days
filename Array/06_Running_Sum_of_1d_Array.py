class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = nums[0]
        ls = [sum]
        for i in range(1,len(nums)):
            sum+=nums[i]
            ls.append(sum)
        return ls