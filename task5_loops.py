# Task 5: Loops

# (a) Numbers 1 to 20 using for loop
print("Numbers from 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")
print("\n")

# (b) Multiplication table of any number
n = int(input("Enter a number for its multiplication table: "))
print(f"\nMultiplication table of {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# (c) Even numbers 1 to 50 using while loop
print("\nEven numbers from 1 to 50:")
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()
