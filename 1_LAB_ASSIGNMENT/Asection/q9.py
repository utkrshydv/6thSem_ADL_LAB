#name: "Utkarsh Yadav" roll: "23053172"
#Find the largest of three numbers.

a, b, c = map(int, input("Enter Three Numbers: ").split(", "))
largest = a if a >= b and a >= c else b if b >= a and b >= c else c
print(f"{largest}")