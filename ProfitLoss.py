cp = int(input("Enter the cost price : "))
sp = int(input("Enter the selling price :"))
if sp>cp :
    print("He made a profit of :",sp-cp)
elif cp>sp :
    print("He incrred loss of :",cp-sp)
else :
    print("No profit No loss")