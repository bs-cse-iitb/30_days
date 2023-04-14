class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """   
        #ls = nums # this will reference the same listnot create new copy
        ls = list(nums)
        j =0 
        k = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if abs(ls[j])> abs(ls[k]):
                nums[i]=ls[j]*ls[j]
                j+=1
            else:
                nums[i]=ls[k]*ls[k]
                k-=1

        return nums