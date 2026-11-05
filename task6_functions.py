# Task 6: Functions
def square(num):
    """Return the square of a number."""
    return num * num

def average(a, b, c):
    """Return the average of three numbers."""
    return (a + b + c) / 3

x = float(input("Enter a number to find its square: "))
print(f"Square of {x} = {square(x)}")

print("\nEnter three numbers to find their average:")
n1 = float(input("Number 1: "))
n2 = float(input("Number 2: "))
n3 = float(input("Number 3: "))
print(f"Average = {average(n1, n2, n3):.2f}")
