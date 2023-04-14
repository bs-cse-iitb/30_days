class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rightsum= sum(nums)-nums[0]
        leftsum = 0
        if rightsum==0:
            return 0
         
        for i in range(1,len(nums)):
            leftsum+=nums[i-1]
            rightsum-=nums[i]
            if (leftsum==rightsum):
                return i
        if leftsum==0:
            return len(nums)-1
        return -1
       