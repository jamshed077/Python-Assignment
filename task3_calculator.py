# Task 3: Operators - Simple Calculator
a = float(input("Enter first number : "))
b = float(input("Enter second number: "))

print("\n----- Results -----")
print(f"Addition       : {a} + {b} = {a + b}")
print(f"Subtraction    : {a} - {b} = {a - b}")
print(f"Multiplication : {a} * {b} = {a * b}")
if b != 0:
    print(f"Division       : {a} / {b} = {a / b}")
    print(f"Modulus        : {a} % {b} = {a % b}")
else:
    print("Division/Modulus: Not possible (second number is zero)")
