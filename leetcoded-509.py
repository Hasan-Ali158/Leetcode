class solution:
    def fibonaccinumber(self,n):
        if n==1 or n==2:
            return 1

        if n==0:
            return 0

        return self.fibonaccinumber(n-1)+self.fibonaccinumber(n-2)

def main():
    n=9
    sol=solution()
    a=sol.fibonaccinumber(n)
    print(a)
main()

