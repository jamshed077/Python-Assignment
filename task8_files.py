# Task 8: Basic File Handling
filename = "introduction.txt"

# 1 & 2. Create file and write introduction
with open(filename, "w") as f:
    f.write("Hello! My name is Jamshed Ali.\n")
    f.write("I study B.S. in Computer Science & Data Analytics at IIT Patna.\n")
    f.write("I am interested in Data Analytics and Python programming.\n")
print(f"'{filename}' created and introduction written.\n")

# 3. Read and display contents
print("File contents:")
print("-" * 30)
with open(filename, "r") as f:
    print(f.read())
print("-" * 30)
