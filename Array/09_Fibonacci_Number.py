class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        if n == 0:
            return a
        elif n==1:
            return b
        else:
            while(n>1):
                c = a+b
                a = b
                b = c
                n-=1
            return c
