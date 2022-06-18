name = input("Enter your Name:")
print("Hello " + name + "!")


num1 = int(input("PLease Enter your first Number: "))
num2 = int(input("Please Enter your second Number: "))

print("Your two numbers are:", num1, "and", num2)

def addNum(num1, num2):
    total = num1 + num2
    return(total)
num1 = int(input("PLease Enter your first Number: "))
num2 = int(input("Please Enter your second Number: "))

print("Total: ", addNum(num1, num2))