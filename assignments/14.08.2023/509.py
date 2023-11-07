class Solution(object):
    def fib(self, n):
        # n = int(input= "Enter the integer"):
        if (n==0 or n==1):
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)