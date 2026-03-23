a = int(input("Enter a number: "))
if a == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
    print("Invalid input. Please enter a valid number.")
    a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if b == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
    print("Invalid input. Please enter a valid number.")
    b = int(input("Enter another number: "))
c = input("Enter an operator (+, -, *, /): ")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
else:
    print("Invalid operator")
    c = input("Enter an operator (+, -, *, /): ")
