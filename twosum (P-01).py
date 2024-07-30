num=[]
n=int(input('Enter n: '))
for i in range(n):
    integers=int(input('Enter inputs: '))
    num.append(integers)
print(num)

target=int(input('Enter target: '))
a=len(num)
for j in range(a-1):
    for k in range(j+1,a):
        if num[j]+num[k]==target:
            print([j,k])


