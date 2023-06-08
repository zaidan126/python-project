# backward Pyramid Pattern
size = 5  # Size of the pyramid pattern

for row in range(size):
    for col in range(row):
        print(" ", end=" ")
    for col in range((size - row) * 2 - 1):
        print("*", end=" ")
    print()