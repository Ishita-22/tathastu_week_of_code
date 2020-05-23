terms=int(input("enter the no. of terms :"))
n=0
a=0
b=1
if terms>0:
    while n<=terms:
        print(a)
        n=a+b
        a=b
        b=n
else:
    print(0)
