# Task 7: Strings & Collections

# ---- String operations ----
print("=== String Operations ===")
s = "Hello Python World"
print("Original :", s)
print("upper()  :", s.upper())
print("lower()  :", s.lower())
print("replace():", s.replace("World", "Students"))
print("find()   :", s.find("Python"))

# ---- List operations ----
print("\n=== List Operations ===")
fruits = ["mango", "apple", "banana"]
print("Original :", fruits)
fruits.append("orange")
print("append() :", fruits)
fruits.remove("banana")
print("remove() :", fruits)
fruits.sort()
print("sort()   :", fruits)

# ---- Tuple ----
print("\n=== Tuple ===")
colors = ("red", "green", "blue")
print("Tuple     :", colors)
print("colors[0] :", colors[0])
print("colors[-1]:", colors[-1])

# ---- Dictionary ----
print("\n=== Dictionary (Student Info) ===")
student = {"name": "Jamshed Ali", "college": "IIT Patna",
           "branch": "CSDA", "year": 1}
for key, value in student.items():
    print(f"{key}: {value}")

# ---- Set ----
print("\n=== Set Operations ===")
nums = {1, 2, 3}
print("Original :", nums)
nums.add(4)
print("add(4)   :", nums)
nums.remove(2)
print("remove(2):", nums)
