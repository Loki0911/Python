import sys
p=True
while p:

    a=int(input("Enter the first number:"))
    b=int(input("Enter the seconnd number:"))
    print("\nOPERATIONS\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.CONTINUE\n6.EXIT")
    o=int(input("Enter the operation you want to perform:"))
    match o:
        case 1:
                print(f"The result is {a+b}")

        case 2:
             print(f"The result is {a-b}")

        case 3:
                print(f"The result is {a*b}")

        case 4:
                if(b!=0):
                    print(f"The result is {float(a/b)}")
                else:
                      print("Can't divide by zero")
        case 5:
                p=True

        case 6:
                p=False

        case default:
                print("NO such operation")
   
    
