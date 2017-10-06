import cs50

print("Height: ", end="")
n = cs50.get_int()

for i in range(1 , n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1 + i):
        print("#", end="")
    print()