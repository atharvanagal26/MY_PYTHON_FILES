marks = float(input("Enter the student mark in % :"))
if marks >= 81 and marks <= 100 :
    print(marks,"Very Good")
elif marks >= 61 and marks <= 80 :
    print(marks,"Good")
elif marks >= 41 and marks <= 60 :
    print(marks,"Average")
elif marks >= 0 and marks <= 40 :
    print("Fail")
else :
    print("Invalid")