def add(list1,list2):
    if len(list1)!=len(list2):
        return invalid

    result=[]
    for i in range(len(list1)):
        result.append(list1[i]+list2[i])

    return result

list1=[2,4,5,2]
list2=[5,3,6,7]

print(add(list1,list2))
