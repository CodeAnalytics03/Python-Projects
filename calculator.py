# Calculator (CFI) program

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero:"
    return x / y

print("*******Simple Calculator*******")
print("Select Operation: ")
print("1. Add (+) : ")
print("2. Subtract (-) : ")
print("3. Multiply (*) : ")
print("4. Divide (/) : ")

print("********************************")
while True:
    choice = input("Enter Your choosen operation (+, -, *, /) : ")
    print(f"You have choosen :  '{choice}' operation")
    print("********************************")

    num1 = float(input("Enter your first Number : "))
    num2 = float(input("Enter your second Number : "))
    print("********************************")
    if choice == '+':
        result = add(num1, num2)
    elif choice == '-':
        result = subtract(num1, num2)
    elif choice == '*':
        result = multiply(num1, num2)
    elif choice == '/':
        result = divide(num1, num2)
    else:
        result = "Invalid Opeartion is choosen, please Choose a valid opeartion (+, -, *, /)"

    print(result)

