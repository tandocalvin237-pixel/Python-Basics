# ------------------------------------------------------------
# Pattern Printing Examples in Python
# Tailored for Beginners
# ------------------------------------------------------------

# 1. Single row of stars
n = int(input("Enter the number of rows you want to print: "))
for j in range(n):
    print("*", end=" ")
print("\n")  # newline for separation

# 2. Single row of hashes
for j in range(4):
    print("# ", end="")
print("\n")

# 3. Another row of hashes
for j in range(4):
    print("# ", end="")
print("\n")

# 4. Square of hashes
for j in range(4):
    for i in range(4):
        print("# ", end=" ")
    print()
print("\n")

# 5. Right triangle of hashes
n = int(input("Enter number of rows: "))
for j in range(n):
    for i in range(j + 1):
        print("# ", end="")
    print()
print("\n")

# 6. Inverted right triangle of hashes
n = int(input("Enter number of rows: "))
for j in range(n):
    for i in range(j, n):
        print("# ", end="")
    print()
print("\n")

# 7. Mixed star-space triangle
n = int(input("Enter number of rows: "))
for j in range(n):
    for i in range(j + 1):
        print("*", end=" ")
    for i in range(j, n):
        print(" ", end=" ")
    print()
print("\n")

# 8. Right-aligned triangle of stars
n = int(input("Enter number of rows: "))
for j in range(n):
    for i in range(j, n):
        print(" ", end=" ")
    for i in range(j + 1):
        print("*", end=" ")
    print()
print("\n")

# 9. Inverted right-aligned triangle of stars
n = int(input("Enter number of rows: "))
for j in range(n):
    for i in range(j + 1):
        print(" ", end=" ")
    for i in range(j, n):
        print("*", end=" ")
    print()
print("\n")

# 10. Diamond-like pattern
n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print("* ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print()
print("\n")

# 11. Simple triangle of stars
rows = 5
for i in range(1, rows + 1):
    print("* " * i)
print("\n")

# 12. Hollow square of stars
rows = 10
for i in range(rows):
    if i == 0 or i == rows - 1:
        print("* " * rows)
    else:
        print("* " + "  " * (rows - 2) + "*  ")
