def add(P , Q):
    return P + Q
def subtract(P , Q):
    return P - Q
def multiply(P , Q):
    return P * Q
def divide(P , Q):
    return P + Q  

print("please select the operations : ") 
print(" a. Add") 
print(" b. Subtract")  
print(" c. Multiply")  
print(" d. Divide")  

choice = input("please enter the choice (a/ b/ c/ d): ")

first = int(input("enter first number : "))
 
second = int(input("enter second number : "))


if choice == "a":
    print(first + second)
elif choice == "b":
    print(first - second)
elif choice == "c":
    print(first * second)
elif choice == "d":
    print(first / second)


else:
    print("invalid choice") 