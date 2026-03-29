num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2st number : "))
o = str(input("Enter Operator : "))

match o :
    case "+" :
        print("Sum is :",num1+num2)
    case "-" :
        print("Difference is :",num1-num2)
    case "*" :
        print("Product is :",num1*num2)
    case "/" :
        print("Quotient is :",num1/num2)
    case "%" :
        print("Remender is ",num1%num2)
    case _ :
        print("Enter a valid operator")
        