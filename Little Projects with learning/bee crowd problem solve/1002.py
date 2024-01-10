""" The formula to calculate the area of a circumference is defined as A = π . R2. Considering to this problem that π = 3.14159: """
n = 3.14159
R = float(input())

A = n * (R ** 2)

print("A={:.4f}".format(A))

# * Use {:.decimal pointf}.format(variable) to print specific floating point
# print(f"A={A:.4f}")


