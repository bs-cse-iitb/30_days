class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ls = [[1]]
        for i in range(1,numRows):
            temp = [0]+ls[-1]+[0]
            ls2=[]
            for j in range(len(ls[-1])+1):
                ls2.append(temp[j]+temp[j+1])
            ls.append(ls2)
        return ls