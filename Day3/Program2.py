n1 = int(input("Enter the size of List 1 : "))
n2 = int(input("Enter the size of List 2 : "))

List1 = []
List2 = []

print("Enter the elements of List 1 : ")
for x in range(0,n1):
    List1.append(input())

print("Enter the elements of List 2 : ")
for x in range(0,n2):
    List2.append(input())

new_list = []
for x in List1:
    for y in List2:
        if x == y:
            new_list.append(x)

print("The intersection of the two lists is :",new_list)
