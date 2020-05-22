cp=float(input("Enter cost price: "))
sp=float(input("Enter selling price: "))
if cp>=sp:
    print("No profit gain")
else:
    print("Profit earned is",sp-cp)
print("Selling price if we want to gain profit of 5% :",cp+0.05*cp)
