n = 5


for i in range(1, n + 1):
    # Print left stars
    for j in range(i):
        print("*", end="")
    # Print spaces
    for j in range(2 * (n - i)):
        print(" ", end="")
    # Print right stars
    for j in range(i):
        print("*", end="")
    print()