#name: "Utkarsh Yadav" roll: "23053172"
# print pyramid pattern of numbers

n = 5

for i in range(1, n+1):
    print(" " * (n - i), end="")

    for j in range(1, i+1):
        print(j, end=" ")

    print()
