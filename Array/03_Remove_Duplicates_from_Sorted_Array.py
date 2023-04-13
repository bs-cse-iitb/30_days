class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i]!=nums[i+1]:
                nums[j]=nums[i]
                j+=1
            if i == len(nums)-1:
                nums[j]=nums[i]
                j+=1
        return j