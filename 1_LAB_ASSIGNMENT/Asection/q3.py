#name: "Utkarsh Yadav" roll: "23053172"
#Swap two variables without using a third variable.
a = input("Enter a variable: ")
b = input("Enter another variable: ")
print(f"Before swapping: a: {a}, b: {b}")
temp = a
a = b
b = temp
print(f"Swapped values: a : {a}, b: {b}")