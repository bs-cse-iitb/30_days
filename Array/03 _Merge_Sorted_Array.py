class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        for i in range(1,m+1):
            nums1[m+n-i] = nums1[m-i]
        
        i=0
        j=n
        k=0
        while j <m+n and k <n:
            if nums1[j]<nums2[k]:
                nums1[i]=nums1[j]
                j+=1
            else:
                nums1[i]=nums2[k]
                k+=1
            i+=1
        while j <m+n:
            nums1[i]=nums1[j]
            j+=1
            i+=1
        while k <n:
            nums1[i]=nums2[k]
            k+=1
            i+=1
