class solution:
    def tribonacci(self,n):
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)

n=25
sol=solution()
a=sol.tribonacci(n)
print(a)

