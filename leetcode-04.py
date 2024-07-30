class solution:
    def median(self,num1,num2):
        merged=num1+num2
        merged.sort()
        total=len(merged)

        if (total%2==1):
            return (float(merged[total//2]))
        else:
            middle1=merged[total//2-1]
            middle2=merged[total//2]
            result=middle1+middle2
            return float((result)/2.0)


def main():
    num1=[1,3,5]
    num2=[2]

    sol=solution()
    a=sol.median(num1,num2)
    print(a)
main()
