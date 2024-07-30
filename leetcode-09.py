class solution:
    def pald(self,x):
        return str(x)==str(x)[::-1]

def main():
    x=121
    sol=solution()
    a=sol.pald(x)
    print(a)
main()
