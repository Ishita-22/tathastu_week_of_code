num = int(input("Enter the size of the list : "))
print("Enter the list elements : ")
List = []
for x in range(0,num):
    List.append(input())

new_list = []
for x in List:
    if x not in new_list:
        new_list.append(x)

print("List after removing the duplicates is :", new_list)
