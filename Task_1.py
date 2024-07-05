import math
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "Error! Division by zero."
    else: 
        return x/y
def mod(x,y):
    if y==0:
        return "Error! Modulus by Zero."
    else:
        return x%y
def pow(x,y):
    return x**y
def square_root(x):
    if(x<0):
        return "Error! Square Root of Negative Number"
    else:
        return math.sqrt(x)
def cal():
    print("Select Operation:")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5 Modulus")
    print("6 Power")
    print("7 Square Root")
    while True:
        choice=int(input("Enter you Choice between 1 to 7: "))
        if choice in [1,2,3,4,5,6]:
            num1=int(input("Enter the First Number: "))
            num2=int(input("Enter the Second Number: "))
        if choice == 1:
           print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == 2:
            print(f"{num1} - {num2} = {sub(num1,num2)}")
        elif choice == 3:
            print(f"{num1} * {num2} = {mul(num1,num2)}")
        elif choice == 4:
            result= div(num1,num2)
            if isinstance(result,(float,int)):
                print(f"{num1} / {num2} = {result}")
            else:
                print(result)
        elif choice == 5:
            result= mod(num1,num2)
            if isinstance(result,(float,int)):
                print(f"{num1} % {num2} = {result}")
            else:
                print(result)
        elif choice == 6:
            print(f"{num1} ** {num2} = {pow(num1, num2)}")
        elif choice == 7:
            num=int(input("Enter a number: "))
            print(f"√{num} = {square_root(num)}")
        else:
            print("Enter a Valid Input")
        next_cal=input("Do you want to continue (yes/no): ")
        if next_cal.lower() !="yes":
            break

if __name__=="__main__":
    cal()
