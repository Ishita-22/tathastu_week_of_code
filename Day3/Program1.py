def Sum(List,size,sum):
    sumList = []
    if size ==1:
        for x in List:
            sumList.append(sum + x)
        return sumList
    L2 = list(List)
    for x in List:
        L2.remove(x)
        sumList.extend(Sum(L2,size-1,sum + x))
    return sumList

def summation(List,size):
    sumList = list(List)
    for x in range(2,size + 1):
        sumList.extend(Sum(List,x,0))
    number = 1
    while True:
        if number not in sumList:
            print("The least integer which is not present in the list and also cannot be represented as the sum of the sub elements of the list is :",number)
            break
        number+=1  


num = int(input("Enter the size of the list : "))
List = []
print("Enter the list elements : ")
for x in range(0,num):
    List.append(int(input()))
summation(List,num)
