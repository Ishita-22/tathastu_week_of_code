string = input("Enter a string : ")
new_str = ""
for x in string:
    if x not in new_str:
        new_str += x
        
print("String after removing the duplicate is :",new_str)
